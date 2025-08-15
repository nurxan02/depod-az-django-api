from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CategoryViewSet, ProductViewSet, AboutPageViewSet, ContactPageViewSet, FooterSettingsViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'about', AboutPageViewSet, basename='about')
router.register(r'contact', ContactPageViewSet, basename='contact')
router.register(r'footer', FooterSettingsViewSet, basename='footer')

urlpatterns = [
    path('', include(router.urls)),
]
