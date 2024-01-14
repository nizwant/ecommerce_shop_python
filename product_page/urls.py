from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:product_id>/", views.detail, name="detail"),
    path(
        "add_to_favorites/<int:product_id>/",
        views.add_to_favorites,
        name="add_to_favorites",
    ),
    path("favorites/", views.favorites, name="favorites"),
    path(
        "favorites/remove/<int:favorite_id>/",
        views.remove_from_favorites,
        name="remove_from_favorites",
    ),
]
