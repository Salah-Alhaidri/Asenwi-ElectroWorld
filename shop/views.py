from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from shop.models import Product

from django.shortcuts import render
from .models import Product, Category

def Home(request):
    # Fetch all categories
    categories = Category.objects.all()
    
    # Create a dictionary to store products grouped by category
    products_by_category = {}
    
    for category in categories:
        # Fetch products for each category
        products = Product.objects.filter(category_name=category)
        products_by_category[category.category_name] = products
        print(products_by_category)
    
    # Pass the grouped products to the template
    context = {
        'products_by_category': products_by_category,
    }
    return render(request, 'shop/home.html', context)

from django.views.generic import DetailView
from .models import Product, Category

class product_detail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        
        # Get the current product
        product = self.get_object()
        
        # Fetch all products in the same category as the current product
        related_products = Product.objects.filter(category_name=product.category_name).exclude(pk=product.pk)
        
        # Add the related products to the context
        context['related_products'] = related_products
        
        return context
    

def privacy_policy(request):
    return render(request,"shop/privacy_policy.html" ) 