from django import forms
from .models import UserProfile
from django.core.validators import RegexValidator


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "birth_date",
            "street_name",
            "street_number",
            "house_number",
            "zip_code",
            "city",
        ]

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = False
