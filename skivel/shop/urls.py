from django.urls import path
from .views import shop_home, ProductDetailView

urlpatterns = [
    path('', shop_home, name='shop_home'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail')
]
