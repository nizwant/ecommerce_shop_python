from django import forms
from .models import UserProfile
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date


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
        widgets = {
            "birth_date": forms.DateInput(attrs={"type": "date"}),
            "zip_code": forms.TextInput(attrs={"placeholder": "xx-xxx"}),
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = False

        self.fields["zip_code"].validators.append(
            RegexValidator(
                regex=r"^\d{2}-\d{3}$",
                message="Zip code must be in the format: xx-xxx",
                code="invalid_zip_code",
            )
        )

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get("birth_date")

        if birth_date and birth_date > date.today():
            raise ValidationError("Birth date cannot be in the future.")

        return birth_date
