from rest_framework import serializers

from applications.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = instance.category.name
        rep['tags'] = [tag.name for tag in instance.tags.all()]
        return rep
