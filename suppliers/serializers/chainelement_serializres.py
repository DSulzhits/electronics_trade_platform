from rest_framework.serializers import ModelSerializer
from suppliers.models import ChainElement


class ChainElementSerializer(ModelSerializer):
    class Meta:
        model = ChainElement
        fields = '__all__'


class ChainElementListSerializer(ModelSerializer):
    class Meta:
        model = ChainElement
        fields = ('name', 'email', 'supplier')


class ChainElementCreateSerializer(ModelSerializer):
    class Meta:
        model = ChainElement
        exclude = ('creation_time',)


class ChainElementUpdateSerializer(ModelSerializer):
    class Meta:
        model = ChainElement
        exclude = ('id', 'creation_time',)
