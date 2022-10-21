from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Prescription

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2"
        )


class Updateprofile(UserChangeForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email"
        )



class PatientSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2"
        )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_Patient = True
        user.save()
        return user


class DoctorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2"
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_Doctor = True
        if commit:
            user.save()
        return user

class Add_file(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = (
            "Title",
            "File"
        )