from django.shortcuts import render
from .models import medicine_group
from .forms import MedicineGroupForm
def medicinegroup_add_view(request):
    form = MedicineGroupForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MedicineGroupForm()
    context = {
        'form' : form
    }
    return render(request,"add.html", context)
# Create your views here.
