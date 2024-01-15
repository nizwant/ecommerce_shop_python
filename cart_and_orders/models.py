from django.db import models
from product_page.models import Product
from django.contrib.auth.models import User


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def total(self):
        return self.product.price * self.quantity


class Order(models.Model):
    SHIPPING_METHODS = [
        ("PACZKOMAT", "Paczkomat"),
        ("PACZKA_ORLEN", "Paczka Orlen"),
        ("POCZTA_POLSKA", "Poczta Polska"),
        ("KURIER", "Kurier"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_method = models.CharField(
        max_length=20, choices=SHIPPING_METHODS, default="Paczkomat"
    )
    shipping_status = models.CharField(
        max_length=20, default="Przygotowanie do wysyłki"
    )
    shipping_street_number = models.CharField(max_length=10)
    shipping_house_number = models.CharField(max_length=10)
    shipping_street_name = models.CharField(max_length=255)
    shipping_zip_code = models.CharField(max_length=10)
    shipping_city = models.CharField(max_length=255)
    shipping_email = models.EmailField(max_length=255)
    shipping_first_name = models.CharField(max_length=255)
    shipping_last_name = models.CharField(max_length=255)
    shipping_phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"OrderItem {self.id} for Order {self.order.id}"
