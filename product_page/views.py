from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Product, Category


# Create your views here.
def index(request):
    categories = Category.objects.all()
    if "category" in request.GET and request.GET["category"]:
        selected_categories = request.GET.getlist("category")
        products = Product.objects.filter(category__id__in=selected_categories)
    else:
        products = Product.objects.all()

    sort_option = request.GET.get("sort", "")
    if sort_option == "name_asc":
        products = products.order_by("name")
    elif sort_option == "name_desc":
        products = products.order_by("-name")
    elif sort_option == "price_asc":
        products = products.order_by("price")
    elif sort_option == "price_desc":
        products = products.order_by("-price")
    elif sort_option == "popularity":
        products = products.order_by("-view_count")

    return render(
        request,
        "products/index.html",
        {"product_list": products, "category_list": categories},
    )


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.view_count += 1
    product.save()
    return render(request, "products/detail.html", {"product": product})
