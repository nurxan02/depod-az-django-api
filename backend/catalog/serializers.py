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
