from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Category, Product
from .serializers import (
    CategorySerializer,
    ProductListSerializer,
    ProductDetailSerializer,
)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    lookup_field = 'key'


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.select_related('category').prefetch_related(
        'images', 'features', 'specs', 'highlights'
    )
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'id']
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductDetailSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            qs = qs.filter(category__key=category)
        return qs

    @action(detail=False, methods=['get'], url_path='by-category/(?P<category>[^/.]+)')
    def by_category(self, request, category=None):
        qs = self.get_queryset().filter(category__key=category)
        page = self.paginate_queryset(qs)
        serializer = ProductListSerializer(page or qs, many=True, context={'request': request})
        if page is not None:
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)
