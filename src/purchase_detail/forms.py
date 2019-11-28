from django import forms

from .models import purchase_detail
class PODetailForm(forms.ModelForm):
    class Meta:
        model = purchase_detail
        exclude = ()