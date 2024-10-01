from django import forms
from .models import Orders


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ["status"]
