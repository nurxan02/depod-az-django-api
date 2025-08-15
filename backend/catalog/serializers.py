from rest_framework import serializers
from .models import Category, Product, ProductImage, ProductFeature, ProductSpec, ProductHighlight


class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'is_main', 'alt', 'order']

    def get_image(self, obj):
        request = self.context.get('request')
        url = obj.image.url
        if request is not None:
            return request.build_absolute_uri(url)
        return url


class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = ['id', 'text', 'order']


class ProductSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpec
        fields = ['id', 'label', 'value', 'order']


class ProductHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductHighlight
        fields = ['id', 'number', 'text', 'order']


class CategorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'key', 'name', 'description', 'image']

    def get_image(self, obj):
        if not obj.image:
            return None
        request = self.context.get('request')
        url = obj.image.url
        if request is not None:
            return request.build_absolute_uri(url)
        return url


class ProductListSerializer(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(slug_field='key', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'main_image']

    def get_main_image(self, obj):
        request = self.context.get('request')
        img = obj.images.filter(is_main=True).first() or obj.images.first()
        if not img:
            return None
        url = img.image.url
        if request is not None:
            return request.build_absolute_uri(url)
        return url


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    features = ProductFeatureSerializer(many=True, read_only=True)
    specs = ProductSpecSerializer(many=True, read_only=True)
    highlights = ProductHighlightSerializer(many=True, read_only=True)
    category = serializers.SlugRelatedField(slug_field='key', read_only=True)


    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'images', 'features', 'specs', 'highlights']


# AboutPage API serializer
from .models import AboutPage, AboutValue, AboutTeamMember, AboutTechFeature, AboutTechStat, ContactPage, ContactWorkingHour, ContactFAQ, FooterSettings

class AboutValueOut(serializers.ModelSerializer):
    class Meta:
        model = AboutValue
        fields = ("icon", "title", "text", "order")

class AboutTeamMemberOut(serializers.ModelSerializer):
    class Meta:
        model = AboutTeamMember
        fields = ("title", "description", "detail", "order")

class AboutTechFeatureOut(serializers.ModelSerializer):
    class Meta:
        model = AboutTechFeature
        fields = ("text", "order")

class AboutTechStatOut(serializers.ModelSerializer):
    class Meta:
        model = AboutTechStat
        fields = ("number", "label", "order")

class AboutPageSerializer(serializers.ModelSerializer):
    values = AboutValueOut(many=True, source='values_items', read_only=True)
    team = AboutTeamMemberOut(many=True, source='team_items', read_only=True)
    # Frontend expects an array of strings for features, not objects
    technology_features = serializers.SerializerMethodField()
    technology_stats = AboutTechStatOut(many=True, source='tech_stat_items', read_only=True)

    class Meta:
        model = AboutPage
        fields = (
            'id', 'title', 'subtitle', 'story',
            'experience_years', 'product_models', 'happy_customers', 'quality_rating',
            'mission', 'vision',
            'values_title', 'values',
            'team_description', 'team',
            'technology_title', 'technology_text', 'technology_features', 'technology_stats',
            'contact_title', 'contact_text',
            'updated_at', 'is_active'
        )

    def get_technology_features(self, obj):
        return [f.text for f in obj.feature_items.all()]


class ContactWorkingHourOut(serializers.ModelSerializer):
    class Meta:
        model = ContactWorkingHour
        fields = ("label", "time", "order")


class ContactFAQOut(serializers.ModelSerializer):
    class Meta:
        model = ContactFAQ
        fields = ("question", "answer", "order")


class ContactPageSerializer(serializers.ModelSerializer):
    working_hours = ContactWorkingHourOut(many=True, read_only=True)
    faqs = ContactFAQOut(many=True, read_only=True)

    class Meta:
        model = ContactPage
        fields = (
            'id', 'is_active',
            'hero_title', 'hero_subtitle',
            'email_primary', 'email_secondary', 'phone_primary', 'phone_secondary', 'address_line1', 'address_line2',
            'form_title', 'form_text',
            'support_title', 'support_text', 'support_phone',
            'catalog_title', 'catalog_text', 'catalog_link',
            'map_section_title', 'map_heading', 'map_address', 'map_button_text', 'map_url',
            'working_hours', 'faqs',
            'updated_at',
        )


class FooterSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterSettings
        fields = ("id", "description", "email", "phone", "bottom_text", "is_active", "updated_at")
