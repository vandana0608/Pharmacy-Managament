from django import forms

from .models import invoice_medicine
class InvoiceMedicineForm(forms.ModelForm):
    class Meta:
        model = invoice_medicine
        exclude = ()
