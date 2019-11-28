from django.shortcuts import render
from .models import invoice 
from .forms import InvoiceForm
def invoice_add_view(request):
    form = InvoiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = InvoiceForm()
    context = {
        'form' : form
    }
    return render(request,"add.html", context)