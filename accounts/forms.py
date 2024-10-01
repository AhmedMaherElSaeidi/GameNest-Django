from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "phone",
            "image",
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "first name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "last name"}),
            "username": forms.TextInput(attrs={"placeholder": "username"}),
            "email": forms.TextInput(attrs={"placeholder": "username@domain"}),
            "password": forms.PasswordInput(attrs={"placeholder": "password"}),
            "phone": forms.TextInput(attrs={"placeholder": "+01234567899"}),
        }
