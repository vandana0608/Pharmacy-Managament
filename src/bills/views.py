from django.shortcuts import render
from .models import bill
from .forms import BillForm
def bill_add_view(request):
    form = BillForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BillForm()
    context = {
        'form' : form
    }
    return render(request,"add.html", context)
# Create your views here.
