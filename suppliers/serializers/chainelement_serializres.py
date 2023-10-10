from rest_framework.serializers import ModelSerializer
from suppliers.models import ChainElement
from rest_framework.relations import SlugRelatedField

"""Add serializers for ChainElement views
(Добавлены сериализаторы для контроллеров ChainElement)"""


class ChainElementSerializer(ModelSerializer):
    supplier = SlugRelatedField(slug_field="name", queryset=ChainElement.objects.all())

    class Meta:
        model = ChainElement
        fields = '__all__'


class ChainElementListSerializer(ModelSerializer):
    supplier = SlugRelatedField(slug_field="name", queryset=ChainElement.objects.all())

    class Meta:
        model = ChainElement
        fields = ('id', 'name', 'email', 'supplier', 'country',)


class ChainElementCreateSerializer(ModelSerializer):
    supplier = SlugRelatedField(slug_field="name", queryset=ChainElement.objects.all())

    class Meta:
        model = ChainElement
        exclude = ('creation_time',)


class ChainElementUpdateSerializer(ModelSerializer):
    debt = ChainElementSerializer(many=False, read_only=True, source='debt.all')

    class Meta:
        model = ChainElement
        exclude = ('id', 'creation_time',)
