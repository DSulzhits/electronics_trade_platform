from rest_framework.serializers import ModelSerializer
from suppliers.models import ChainElement, Product
from rest_framework.relations import SlugRelatedField

"""Add serializers for Product views
(Добавлены сериализаторы для контроллеров Product)"""


class ProductSerializer(ModelSerializer):
    seller = SlugRelatedField(slug_field="name", queryset=ChainElement.objects.all())

    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(ModelSerializer):
    seller = SlugRelatedField(slug_field="name", queryset=ChainElement.objects.all())

    class Meta:
        model = Product
        fields = ('id', 'name', 'seller',)


class ProductCreateSerializer(ModelSerializer):
    seller = SlugRelatedField(slug_field="name", queryset=ChainElement.objects.all())

    class Meta:
        model = Product
        exclude = ('created_at',)


class ProductUpdateSerializer(ModelSerializer):
    seller = SlugRelatedField(slug_field="name", queryset=ChainElement.objects.all())

    class Meta:
        model = Product
        exclude = ('id', 'created_at',)
