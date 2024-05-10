from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from . import views

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.getProductList),
    # path('read/<str:req_product_id>', views.getProductbyId),
]