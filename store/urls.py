from django.urls import path
from . import views

app_name = 'store'
urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.product_list, name='product_list'),
    path('shop/<int:category_id>/<int:product_id>/', views.product_detail, name='product_detail'),
    path('search/', views.product_list, name='search'),
    path('contact/', views.contact, name='contact'),
]