from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.sessions.models import Session
from .models import Product, FavoriteProduct, Category
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


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


def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    session = Session.objects.get(session_key=request.session.session_key)
    if not FavoriteProduct.objects.filter(session=session, product=product).exists():
        FavoriteProduct.objects.create(session=session, product=product)
    return redirect("index")


@login_required
def favorites(request):
    favorites = FavoriteProduct.objects.filter(session=request.session.session_key)
    return render(request, "products/favorites.html", {"favorites": favorites})


@require_POST
def remove_from_favorites(request, favorite_id):
    favorite = get_object_or_404(FavoriteProduct, pk=favorite_id)
    favorite.delete()
    return redirect("favorites")
