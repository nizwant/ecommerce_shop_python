from django.contrib import admin
from .models import Order, OrderItem, CartItem

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(CartItem)
