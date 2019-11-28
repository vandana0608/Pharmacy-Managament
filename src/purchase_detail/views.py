from django.shortcuts import render
from .models import purchase_detail
from .forms import PODetailForm
def purchase_detail_view(request):
    obj = purchase_detail.objects.all()
    context = {
        'object' : obj
    }
    return render(request,"purchaseorder/detail.html", context)

def pod_add_view(request):
    form = PODetailForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PODetailForm()
    context = {
        'form' : form
    }
    return render(request,"add.html", context)
# Create your views here.
