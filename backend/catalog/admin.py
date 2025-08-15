from django.contrib import admin
from .models import (
    Category, Product, ProductImage, ProductFeature, ProductSpec, ProductHighlight,
    AboutPage, AboutValue, AboutTeamMember, AboutTechFeature, AboutTechStat,
    ContactPage, ContactWorkingHour, ContactFAQ, FooterSettings
)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductFeatureInline(admin.TabularInline):
    model = ProductFeature
    extra = 1


class ProductSpecInline(admin.TabularInline):
    model = ProductSpec
    extra = 1


class ProductHighlightInline(admin.TabularInline):
    model = ProductHighlight
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_filter = ('category',)
    search_fields = ('id', 'name', 'description')
    inlines = [ProductImageInline, ProductFeatureInline, ProductSpecInline, ProductHighlightInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('key', 'name')
    search_fields = ('key', 'name', 'description')
    fields = ('key', 'name', 'description', 'image')


admin.site.site_header = 'Depod Admin'
admin.site.site_title = 'Depod Admin'
admin.site.index_title = 'Depod Administration'


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("title",)
    list_editable = ("is_active",)
    readonly_fields = ("updated_at",)
    fieldsets = (
        ("Başlıq", {"fields": ("title", "subtitle", "is_active")}),
        ("Hekayə & Statistika", {"fields": ("story", "experience_years", "product_models", "happy_customers", "quality_rating")}),
        ("Missiya & Vizyon", {"fields": ("mission", "vision")}),
        ("Dəyərlər Bölməsi", {"fields": ("values_title",)}),
        ("Komanda Bölməsi", {"fields": ("team_description",)}),
        ("Texnologiya", {"fields": ("technology_title", "technology_text")}),
        ("Əlaqə", {"fields": ("contact_title", "contact_text")}),
        ("Sistem", {"fields": ("updated_at",)}),
    )

    actions = ["make_active"]

    def make_active(self, request, queryset):
        # Set only the first selected as active and others inactive
        first = queryset.first()
        if first:
            type(first).objects.exclude(pk=first.pk).update(is_active=False)
            first.is_active = True
            first.save()
        self.message_user(request, "Seçilən səhifə aktiv edildi. Digərləri deaktiv oldu.")
    make_active.short_description = "Seçiləni aktiv et"

class AboutValueInline(admin.TabularInline):
    model = AboutValue
    extra = 1
    fields = ("order", "icon", "title", "text")
    ordering = ("order", "id")

class AboutTeamMemberInline(admin.TabularInline):
    model = AboutTeamMember
    extra = 1
    fields = ("order", "title", "description", "detail")
    ordering = ("order", "id")

class AboutTechFeatureInline(admin.TabularInline):
    model = AboutTechFeature
    extra = 1
    fields = ("order", "text")
    ordering = ("order", "id")

class AboutTechStatInline(admin.TabularInline):
    model = AboutTechStat
    extra = 1
    fields = ("order", "number", "label")
    ordering = ("order", "id")

AboutPageAdmin.inlines = [
    AboutValueInline,
    AboutTeamMemberInline,
    AboutTechFeatureInline,
    AboutTechStatInline,
]


class ContactWorkingHourInline(admin.TabularInline):
    model = ContactWorkingHour
    extra = 1
    fields = ("order", "label", "time")
    ordering = ("order", "id")


class ContactFAQInline(admin.TabularInline):
    model = ContactFAQ
    extra = 1
    fields = ("order", "question", "answer")
    ordering = ("order", "id")


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ("hero_title", "is_active", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("hero_title",)
    readonly_fields = ("updated_at",)
    list_editable = ("is_active",)
    fieldsets = (
        ("Hero", {"fields": ("hero_title", "hero_subtitle", "is_active")}),
        ("Əlaqə Məlumatı", {"fields": ("email_primary", "email_secondary", "phone_primary", "phone_secondary", "address_line1", "address_line2")}),
        ("Əlaqə Forması", {"fields": ("form_title", "form_text")}),
        ("Sidebar Dəstək", {"fields": ("support_title", "support_text", "support_phone")}),
        ("Sidebar Kataloq", {"fields": ("catalog_title", "catalog_text", "catalog_link")}),
        ("Xəritə", {"fields": ("map_section_title", "map_heading", "map_address", "map_button_text", "map_url")}),
        ("Sistem", {"fields": ("updated_at",)}),
    )

    actions = ["make_active"]

    def make_active(self, request, queryset):
        first = queryset.first()
        if first:
            type(first).objects.exclude(pk=first.pk).update(is_active=False)
            first.is_active = True
            first.save()
        self.message_user(request, "Seçilən kontakt səhifəsi aktiv edildi. Digərləri deaktiv oldu.")
    make_active.short_description = "Seçiləni aktiv et"

    inlines = [ContactWorkingHourInline, ContactFAQInline]


@admin.register(FooterSettings)
class FooterSettingsAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "is_active", "updated_at")
    list_filter = ("is_active",)
    readonly_fields = ("updated_at",)
    list_editable = ("is_active",)
    fields = ("description", "email", "phone", "bottom_text", "is_active", "updated_at")
    actions = ["make_active"]

    def make_active(self, request, queryset):
        first = queryset.first()
        if first:
            type(first).objects.exclude(pk=first.pk).update(is_active=False)
            first.is_active = True
            first.save()
        self.message_user(request, "Aktiv footer dəyişdirildi.")
    make_active.short_description = "Seçiləni aktiv et"
