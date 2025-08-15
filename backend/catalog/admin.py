from django.contrib import admin
from .models import Category, Product, ProductImage, ProductFeature, ProductSpec, ProductHighlight


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
