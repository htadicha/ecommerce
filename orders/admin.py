from django.contrib import admin
from .models import Order, OrderProduct

class OrderProductInline(admin.TabularInline):
    """
    Allows editing of products directly within the Order page in the admin panel.
    """
    model = OrderProduct
    readonly_fields = ('product', 'quantity', 'product_price', 'user')
    extra = 0 # Don't show any extra empty forms

class OrderAdmin(admin.ModelAdmin):
    """
    Customizes the display of Orders in the admin panel.
    """
    list_display = ['order_number', 'full_name', 'phone', 'email', 'order_total', 'status', 'is_ordered', 'created_at']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name', 'last_name', 'phone', 'email']
    list_per_page = 20
    inlines = [OrderProductInline] # Add the inline here

    # A helper method to display the user's full name
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
