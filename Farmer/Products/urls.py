from django.urls import path
from . import views
from .models import Product

urlpatterns = [
    path('', views.homepage),
    path('additem/<id1>/', views.additem),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_increment1/<int:id>/',
         views.item_increment1, name='item_increment1'),
    path('cart/item_increment10/<int:id>/',
         views.item_increment10, name='item_increment10'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/item_decrement1/<int:id>/',
         views.item_decrement1, name='item_decrement1'),
    path('cart/item_decrement10/<int:id>/',
         views.item_decrement10, name='item_decrement10'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
]
