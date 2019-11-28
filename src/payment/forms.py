from django import forms

from .models import payment
class PaymentForm(forms.ModelForm):
    class Meta:
        model = payment
        exclude = ()