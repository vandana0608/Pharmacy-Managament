from django.shortcuts import render
from .models import purchaseorder
from .forms import POForm
def po_add_view(request):
    form = POForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = POForm()
    context = {
        'form' : form
    }
    return render(request,"add.html", context)
# Create your views here.
