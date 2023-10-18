from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from suppliers.serializers.chainelement_serializres import ChainElementSerializer, ChainElementListSerializer, \
    ChainElementCreateSerializer, ChainElementUpdateSerializer
from suppliers.serializers.product_serializers import ProductSerializer, ProductListSerializer, ProductCreateSerializer, \
    ProductUpdateSerializer
from users.permissions import IsActive, IsSuperuser, IsModerator

from suppliers.models import ChainElement, Product

"""Add CRUD endpoints for Models: ChainElement, Product
(Добавлен CRUD для Модели: ChainElement, Product)"""


class ChainElementListAPIView(ListAPIView):
    serializer_class = ChainElementListSerializer
    permission_classes = [IsAuthenticated, IsActive]

    def get_queryset(self):
        queryset = ChainElement.objects.all()
        country = self.request.query_params.get('country')
        if country is not None:
            queryset = queryset.filter(country=country)
        return queryset


class ChainElementCreateAPIView(CreateAPIView):
    serializer_class = ChainElementCreateSerializer
    queryset = ChainElement.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ChainElementRetrieveAPIView(RetrieveAPIView):
    serializer_class = ChainElementSerializer
    queryset = ChainElement.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ChainElementUpdateAPIView(UpdateAPIView):
    serializer_class = ChainElementUpdateSerializer
    queryset = ChainElement.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ChainElementDestroyAPIView(DestroyAPIView):
    serializer_class = ChainElementSerializer
    queryset = ChainElement.objects.all()
    permission_classes = [IsAuthenticated, IsActive, IsModerator | IsSuperuser]


class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = ChainElement.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductRetrieveAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = ChainElement.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductUpdateAPIView(UpdateAPIView):
    serializer_class = ProductUpdateSerializer
    queryset = ChainElement.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductDestroyAPIView(DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = ChainElement.objects.all()
    permission_classes = [IsAuthenticated, IsActive, IsModerator | IsSuperuser]
