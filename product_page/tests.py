from django.test import TestCase, Client
from decimal import Decimal
from .models import Product, Category, FavoriteProduct
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware
from django.test.client import RequestFactory
from django.contrib.sessions.models import Session


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name="Test Category")
        Product.objects.create(
            name="Test Product",
            price=Decimal("10.00"),
            category=Category.objects.get(id=1),
        )

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field("name").verbose_name
        self.assertEquals(field_label, "name")

    def test_price_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field("price").verbose_name
        self.assertEquals(field_label, "price")

    def test_category_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field("category").verbose_name
        self.assertEquals(field_label, "category")

    def test_product_object_name(self):
        product = Product.objects.get(id=1)
        expected_object_name = f"{product.name}"
        self.assertEquals(expected_object_name, str(product))


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(name="Test Category")

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field("name").verbose_name
        self.assertEquals(field_label, "name")


class ProductViewsTest(TestCase):
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

    def setUp(self):
        # Set up client for each test
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.get(username="testuser")

    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")
        self.assertTemplateUsed(response, "products/index.html")

    def test_detail_view(self):
        response = self.client.get(reverse("detail", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")
        self.assertTemplateUsed(response, "products/detail.html")

    def test_add_to_favorites_view(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("add_to_favorites", args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_favorites_view(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("favorites"))
        self.assertEqual(response.status_code, 200)
