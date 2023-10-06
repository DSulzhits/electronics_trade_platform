from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from suppliers.serializers.chainelement_serializres import ChainElementSerializer, ChainElementListSerializer, \
    ChainElementCreateSerializer, ChainElementUpdateSerializer
from users.permissions import IsActive, IsSuperuser, IsModerator

from suppliers.models import ChainElement


class ChainElementListAPIView(ListAPIView):
    serializer_class = ChainElementListSerializer
    queryset = ChainElement.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


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
