from django import forms

from .models import bill
class BillForm(forms.ModelForm):
    class Meta:
        model = bill
        exclude = ()