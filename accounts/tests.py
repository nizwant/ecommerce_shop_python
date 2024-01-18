from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile
from datetime import date


class UserProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        # Set up non-modified objects used by all test methods
        self.user = User.objects.create(username="testuser", password="12345")
        self.user.userprofile.phone_number = "1234567890"
        self.user.userprofile.street_number = "10"
        self.user.userprofile.house_number = "10"
        self.user.userprofile.street_name = "Test Street"
        self.user.userprofile.zip_code = "12345"
        self.user.userprofile.city = "Test City"
        self.user.userprofile.birth_date = date(2000, 1, 1)
        self.user.userprofile.email = "test@test.com"
        self.user.userprofile.first_name = "Test"
        self.user.userprofile.last_name = "User"
        self.user.userprofile.save()

    def test_user_label(self):
        user_profile = UserProfile.objects.get(id=1)
        field_label = user_profile._meta.get_field("user").verbose_name
        self.assertEquals(field_label, "user")

    def test_phone_number_label(self):
        user_profile = UserProfile.objects.get(id=1)
        field_label = user_profile._meta.get_field("phone_number").verbose_name
        self.assertEquals(field_label, "phone number")

    def test_street_number_label(self):
        user_profile = UserProfile.objects.get(id=1)
        field_label = user_profile._meta.get_field("street_number").verbose_name
        self.assertEquals(field_label, "street number")

    def test_house_number_label(self):
        user_profile = UserProfile.objects.get(id=1)
        field_label = user_profile._meta.get_field("house_number").verbose_name
        self.assertEquals(field_label, "house number")

    def test_street_name_label(self):
        user_profile = UserProfile.objects.get(id=1)
        field_label = user_profile._meta.get_field("street_name").verbose_name
        self.assertEquals(field_label, "street name")

    def test_zip_code_label(self):
        user_profile = UserProfile.objects.get(id=1)
        field_label = user_profile._meta.get_field("zip_code").verbose_name
        self.assertEquals(field_label, "zip code")

    def test_city_label(self):
        user_profile = UserProfile.objects.get(id=1)
        field_label = user_profile._meta.get_field("city").verbose_name
        self.assertEquals(field_label, "city")

    def test_birth_date_label(self):
        user_profile = UserProfile.objects.get(id=1)
        field_label = user_profile._meta.get_field("birth_date").verbose_name
        self.assertEquals(field_label, "birth date")

    def test_email_label(self):
        user_profile = UserProfile.objects.get(id=1)
        field_label = user_profile._meta.get_field("email").verbose_name
        self.assertEquals(field_label, "email")

    def test_first_name_label(self):
        user_profile = UserProfile.objects.get(id=1)
        field_label = user_profile._meta.get_field("first_name").verbose_name
        self.assertEquals(field_label, "first name")

    def test_last_name_label(self):
        user_profile = UserProfile.objects.get(id=1)
        field_label = user_profile._meta.get_field("last_name").verbose_name
        self.assertEquals(field_label, "last name")

    def test_profile_created(self):
        # Check that a UserProfile instance has been created
        self.assertTrue(UserProfile.objects.filter(user=self.user).exists())

    def test_profile_saved(self):
        # Update the UserProfile instance
        self.user.userprofile.birth_date = date(2001, 1, 1)
        self.user.userprofile.save()

        # Retrieve the updated UserProfile instance from the database
        updated_profile = UserProfile.objects.get(user=self.user)

        # Check that the UserProfile instance has been saved
        self.assertEqual(updated_profile.birth_date, date(2001, 1, 1))
