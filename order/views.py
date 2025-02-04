from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
from .models import Cart, Order
from shop.models import Product

# Add to Cart View
class AddToCartView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        item = get_object_or_404(Product, pk=pk)
        order_item, created = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        
        if order_qs.exists():
            order = order_qs[0]
            if order.orderitems.filter(item=item).exists():
                order_item.quantity += 1
                order_item.save()
                messages.info(request, "This item quantity was updated.")
            else:
                order.orderitems.add(order_item)
                messages.info(request, "This item was added to your cart.")
        else:
            order = Order.objects.create(user=request.user)
            order.orderitems.add(order_item)
            messages.info(request, "This item was added to your cart.")
        
        return redirect("shop:home")
# order/views.py or shop/views.py
from django.shortcuts import render
from .models import Cart, Order

def checkout(request):
    # Fetch the user's cart and order details
    carts = Cart.objects.filter(user=request.user)
    order = Order.objects.filter(user=request.user).first()

    context = {
        'carts': carts,
        'order': order,
    }
    return render(request, 'order/checkout.html', context)
# Cart View
class CartView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        carts = Cart.objects.filter(user=request.user, purchased=False)
        orders = Order.objects.filter(user=request.user, ordered=False)
        
        if carts.exists() and orders.exists():
            order = orders[0]
            return render(request, 'order/cart.html', context={'carts': carts, 'order': order})
        else:
            messages.warning(request, "You don't have any item in your cart.")
            return redirect("shop:home")

# Remove from Cart View
class RemoveFromCartView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        item = get_object_or_404(Product, pk=pk)
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        
        if order_qs.exists():
            order = order_qs[0]
            if order.orderitems.filter(item=item).exists():
                order_item = Cart.objects.filter(item=item, user=request.user, purchased=False).first()
                order.orderitems.remove(order_item)
                order_item.delete()
                messages.warning(request, "This item was removed from your cart.")
                return redirect("order:cart")
            else:
                messages.info(request, "This item was not in your cart.")
                return redirect("order:home")
        else:
            messages.info(request, "You don't have any active order.")
            return redirect("order:home")

# Increase Cart Quantity View
class IncreaseCartView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        item = get_object_or_404(Product, pk=pk)
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        
        if order_qs.exists():
            order = order_qs[0]
            if order.orderitems.filter(item=item).exists():
                order_item = Cart.objects.filter(item=item, user=request.user, purchased=False).first()
                if order_item.quantity < item.available_quantity:
                    order_item.quantity += 1
                    order_item.save()
                    messages.success(request, f"{item.name} quantity was updated to {order_item.quantity}.")
                else:
                    messages.warning(request, f"Cannot increase quantity. Only {item.available_quantity} available for {item.name}.")
            else:
                messages.warning(request, f"{item.name} is not in your cart.")
                return redirect("shop:home")
        else:
            messages.warning(request, "You don't have any active order.")
            return redirect("shop:home")
        
        return redirect("order:cart")

# Decrease Cart Quantity View
class DecreaseCartView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        item = get_object_or_404(Product, pk=pk)
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        
        if order_qs.exists():
            order = order_qs[0]
            if order.orderitems.filter(item=item).exists():
                order_item = Cart.objects.filter(item=item, user=request.user, purchased=False).first()
                if order_item.quantity > 1:
                    order_item.quantity -= 1
                    order_item.save()
                    messages.info(request, f"{item.name} quantity was updated.")
                else:
                    order.orderitems.remove(order_item)
                    order_item.delete()
                    messages.info(request, f"{item.name} was removed from your cart.")
                return redirect("order:cart")
            else:
                messages.info(request, f"{item.name} is not in your cart.")
                return redirect("shop:home")
        else:
            messages.info(request, "You don't have any active order.")
            return redirect("shop:home")