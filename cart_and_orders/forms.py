from django import forms
from .models import Order
from accounts.models import UserProfile


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "shipping_first_name",
            "shipping_last_name",
            "shipping_email",
            "shipping_phone_number",
            "shipping_street_name",
            "shipping_street_number",
            "shipping_house_number",
            "shipping_zip_code",
            "shipping_city",
            "shipping_method",
        ]
        labels = {
            "shipping_first_name": "First name",
            "shipping_last_name": "Last name",
            "shipping_email": "Email",
            "shipping_phone_number": "Phone number",
            "shipping_street_name": "Street name",
            "shipping_street_number": "Street number",
            "shipping_house_number": "House number",
            "shipping_zip_code": "Zip code",
            "shipping_city": "City",
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(OrderForm, self).__init__(*args, **kwargs)
        if user:
            profile = UserProfile.objects.get(user=user)
            for field_name in self.fields:
                field_name_modify = field_name.replace("shipping_", "")
                if field_name_modify in profile.__dict__:
                    self.fields[field_name].initial = profile.__dict__[
                        field_name_modify
                    ]
