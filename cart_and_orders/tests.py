from django.test import TestCase
from decimal import Decimal
from .models import OrderItem, CartItem, Order
from product_page.models import Product, Category
from django.contrib.auth.models import User


class OrderItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create_user(username="testuser", password="12345")
        Order.objects.create(
            shipping_street_name="Test Street", user=User.objects.get(id=1)
        )
        OrderItem.objects.create(
            product_name="Test Product",
            product_price=Decimal("10.00"),
            quantity=1,
            order=Order.objects.get(id=1),
        )

    def test_product_name_label(self):
        order_item = OrderItem.objects.get(id=1)
        field_label = order_item._meta.get_field("product_name").verbose_name
        self.assertEquals(field_label, "product name")

    def test_product_price_label(self):
        order_item = OrderItem.objects.get(id=1)
        field_label = order_item._meta.get_field("product_price").verbose_name
        self.assertEquals(field_label, "product price")

    def test_quantity_label(self):
        order_item = OrderItem.objects.get(id=1)
        field_label = order_item._meta.get_field("quantity").verbose_name
        self.assertEquals(field_label, "quantity")

    def test_order_label(self):
        order_item = OrderItem.objects.get(id=1)
        field_label = order_item._meta.get_field("order").verbose_name
        self.assertEquals(field_label, "order")


class CartItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name="Test Category")
        Product.objects.create(
            name="Test Product",
            price=Decimal("10.00"),
            category=Category.objects.get(id=1),
        )
        User.objects.create_user(username="testuser", password="12345")
        CartItem.objects.create(
            product=Product.objects.get(id=1),
            quantity=1,
            user=User.objects.get(username="testuser"),
        )

    def test_product_label(self):
        cart_item = CartItem.objects.get(id=1)
        field_label = cart_item._meta.get_field("product").verbose_name
        self.assertEquals(field_label, "product")


class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create_user("testuser", "test@test.com", "testpassword")
        Order.objects.create(
            user=User.objects.get(username="testuser"),
            shipping_method="Paczkomat",
            shipping_status="Przygotowanie do wysyłki",
            shipping_street_number="10",
            shipping_house_number="10",
            shipping_street_name="Test Street",
            shipping_zip_code="12345",
            shipping_city="Test City",
            shipping_email="test@test.com",
            shipping_first_name="Test",
            shipping_last_name="User",
            shipping_phone_number="1234567890",
            total_price=Decimal("10.00"),
        )

    def test_user_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field("user").verbose_name
        self.assertEquals(field_label, "user")

    def test_created_at_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field("created_at").verbose_name
        self.assertEquals(field_label, "created at")

    def test_shipping_method_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field("shipping_method").verbose_name
        self.assertEquals(field_label, "shipping method")

    def test_shipping_status_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field("shipping_status").verbose_name
        self.assertEquals(field_label, "shipping status")

    def test_shipping_street_number_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field("shipping_street_number").verbose_name
        self.assertEquals(field_label, "shipping street number")

    def test_shipping_house_number_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field("shipping_house_number").verbose_name
        self.assertEquals(field_label, "shipping house number")

    def test_shipping_street_name_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field("shipping_street_name").verbose_name
        self.assertEquals(field_label, "shipping street name")

    def test_shipping_zip_code_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field("shipping_zip_code").verbose_name
        self.assertEquals(field_label, "shipping zip code")

    def test_shipping_city_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field("shipping_city").verbose_name
        self.assertEquals(field_label, "shipping city")

    def test_shipping_email_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field("shipping_email").verbose_name
        self.assertEquals(field_label, "shipping email")

    def test_shipping_first_name_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field("shipping_first_name").verbose_name
        self.assertEquals(field_label, "shipping first name")

    def test_shipping_last_name_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field("shipping_last_name").verbose_name
        self.assertEquals(field_label, "shipping last name")

    def test_shipping_phone_number_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field("shipping_phone_number").verbose_name
        self.assertEquals(field_label, "shipping phone number")

    def test_total_price_label(self):
        order = Order.objects.get(id=1)
        field_label = order._meta.get_field("total_price").verbose_name
        self.assertEquals(field_label, "total price")
