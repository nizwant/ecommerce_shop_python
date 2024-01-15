from django.shortcuts import render, redirect
from .models import CartItem
from product_page.models import Product


# Create your views here.
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, "cart_and_orders/cart.html", {"cart_items": cart_items})


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={"quantity": 1},
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect("cart")
