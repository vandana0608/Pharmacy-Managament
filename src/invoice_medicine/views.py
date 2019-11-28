from django.shortcuts import render
from .models import invoice_medicine
from .forms import InvoiceMedicineForm
def invoice_medicine_detail_view(request):
    obj = invoice_medicine.objects.get()
    context = {
        'object' : obj
    }
    return render(request,"invoice/detail.html", context)

def invoicemedicine_add_view(request):
    form = InvoiceMedicineForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = InvoiceMedicineForm()
    context = {
        'form' : form
    }
    return render(request,"add.html", context)