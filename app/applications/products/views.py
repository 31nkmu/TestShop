from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from applications.products import serializers
from applications.products.models import Product


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('category').prefetch_related('tags').all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @method_decorator(cache_page(60 * 15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
