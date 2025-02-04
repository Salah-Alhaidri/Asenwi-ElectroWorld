from django.urls import path
from . import views
app_name = 'shop'

urlpatterns = [
    path('', views.Home, name='home'),
    path('product/<pk>/', views.product_detail.as_view(), name='product_detail'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),


]
