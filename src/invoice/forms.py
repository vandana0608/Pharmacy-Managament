from django import forms

from .models import invoice
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = invoice
        exclude = ()
