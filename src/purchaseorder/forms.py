from django import forms

from .models import purchaseorder
class POForm(forms.ModelForm):
    class Meta:
        model = purchaseorder
        exclude = ()