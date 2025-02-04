from django.contrib import admin
from .models import Cart, Order

# Custom Admin Class for Cart
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'item', 'quantity', 'purchased', 'created', 'updated', 'get_total')
    list_filter = ('purchased', 'created', 'updated')
    search_fields = ('user__username', 'item__name')
    list_editable = ('quantity', 'purchased')
    list_per_page = 20

    def get_total(self, obj):
        return obj.get_total()
    get_total.short_description = 'Total Price'

# Custom Admin Class for Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'ordered', 'created', 'paymentId', 'orderId', 'get_totals')
    list_filter = ('ordered', 'created')
    search_fields = ('user__username', 'paymentId', 'orderId')
    list_editable = ('ordered',)
    list_per_page = 20

    def get_totals(self, obj):
        return obj.get_totals()
    get_totals.short_description = 'Total Order Price'

# Register the models with their custom admin classes
admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)