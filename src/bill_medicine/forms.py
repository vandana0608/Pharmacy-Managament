from django import forms

from .models import bill_medicine
class BillMedicineForm(forms.ModelForm):
    class Meta:
        model = bill_medicine
        exclude = ()