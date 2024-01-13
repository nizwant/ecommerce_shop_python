from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Product


# Create your views here.
def index(request):
    product_list = Product.objects.order_by("name")
    context = {"product_list": product_list}
    return render(request, "products/index.html", context)


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "products/detail.html", {"product": product})
