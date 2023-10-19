from django.urls import path
from rest_framework.routers import DefaultRouter
from suppliers.apps import SuppliersConfig
from suppliers.views import ChainElementListAPIView, ChainElementCreateAPIView, ChainElementRetrieveAPIView, \
    ChainElementUpdateAPIView, ChainElementDestroyAPIView, ProductListAPIView, ProductCreateAPIView, \
    ProductRetrieveAPIView, ProductUpdateAPIView, ProductDestroyAPIView

app_name = SuppliersConfig.name

router = DefaultRouter()

urlpatterns = [
    # ChainElement urlpatterns
    path('chain_elements/', ChainElementListAPIView.as_view(), name='chain_elements_list'),
    path('chain_element/create/', ChainElementCreateAPIView.as_view(), name='chain_element_create'),
    path('chain_element/<int:pk>/', ChainElementRetrieveAPIView.as_view(), name='chain_element_detail'),
    path('chain_element/<int:pk>/update/', ChainElementUpdateAPIView.as_view(), name='chain_element_update'),
    path('chain_element/<int:pk>/delete', ChainElementDestroyAPIView.as_view(), name='chain_element_delete'),

    # Product urlpatterns
    path('products/', ProductListAPIView.as_view(), name='products_list'),
    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_detail'),
    path('product/<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDestroyAPIView.as_view(), name='product_delete'),
] + router.urls
