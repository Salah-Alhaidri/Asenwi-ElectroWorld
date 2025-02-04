

from django.urls import path
from .views import AddToCartView, CartView, RemoveFromCartView, IncreaseCartView, DecreaseCartView,checkout

app_name = 'order'

urlpatterns = [
    path('add-to-cart/<int:pk>/', AddToCartView.as_view(), name='add'),
    path('cart/', CartView.as_view(), name='cart'),
    path('remove-from-cart/<int:pk>/', RemoveFromCartView.as_view(), name='remove'),
    path('increase-cart/<int:pk>/', IncreaseCartView.as_view(), name='increase'),
    path('decrease-cart/<int:pk>/', DecreaseCartView.as_view(), name='decrease'),
    path('checkout/', checkout, name='checkout'),  # Add this line

]