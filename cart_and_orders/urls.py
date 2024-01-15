from django.urls import path

from . import views

urlpatterns = [
    path("cart/", views.cart, name="cart"),
    path("add_to_cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("update_quantity/", views.update_quantity, name="update_quantity"),
    path("remove_item/", views.remove_item, name="remove_item"),
]
