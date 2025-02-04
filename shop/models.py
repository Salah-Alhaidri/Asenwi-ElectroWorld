from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('-created_dt',)

class Product(models.Model):
    prodect_image = models.ImageField(upload_to='Products')
    name = models.CharField(max_length=100)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    preview_text = models.TextField(max_length=300, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=300, verbose_name='Description')
    price = models.DecimalField(max_digits=11, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    available_quantity = models.PositiveIntegerField(default=0)  # Add this line

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)
