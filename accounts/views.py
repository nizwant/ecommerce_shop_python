from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from cart_and_orders.models import Order, OrderItem


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def user_profile_detail_view(request):
    user_profile = request.user.userprofile
    orders = Order.objects.filter(user=request.user)
    orders = orders.order_by("-created_at")
    return render(
        request,
        "registration/profile_detail.html",
        {"user_profile": user_profile, "orders": orders},
    )


@login_required
def user_profile_order_view(request, order_id):
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order_id=order_id)
    return render(
        request,
        "registration/profile_order.html",
        {"order": order, "order_items": order_items},
    )


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "registration/profile_update.html"
    success_url = reverse_lazy("profile_detail")

    def get_object(self):
        return self.request.user.userprofile
