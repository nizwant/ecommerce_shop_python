from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("profile/update", views.UserProfileUpdateView.as_view(), name="profile"),
    path("profile/", views.user_profile_detail_view, name="profile_detail"),
]
