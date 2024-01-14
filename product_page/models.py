from django.db import models
from django.contrib.sessions.models import Session


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    view_count = models.IntegerField(default=0)
    description = models.TextField()
    main_image = models.ImageField(upload_to="Products", default="Products/No-img.jpg")
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    review_score = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class FavoriteProduct(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
