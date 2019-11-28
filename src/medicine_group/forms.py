from django import forms

from .models import medicine_group
class MedicineGroupForm(forms.ModelForm):
    class Meta:
        model = medicine_group
        exclude = ()
