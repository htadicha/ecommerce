from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('delete/<int:cart_item_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('update/', views.update_cart, name='update_cart'),
    
    
]