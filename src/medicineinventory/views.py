from django.shortcuts import render,redirect
from .models import medicineinventory
from datetime import datetime
import json
import random
global data
global i

# Create your views here.
def medicineinventory_detail_view(request):
    obj = medicineinventory.objects.all()
    context = {
        'object' : obj
    }
    return render(request,"medicine/detail.html", context)

# # def medicineinventory_add_view(request):
# #     form = MedicineInventoryForm(request.POST or None)
# #     if form.is_valid():
# #         form.save()
# #         form = MedicineInventoryForm()
# #     context = {
# #         'form' : form
# #     }
# #     return render(request,"add.html", context)


# # def medicineinventory_update_quantity_view(request,medicine_id):
# #     obj = get_object_or_404(medicineinventory,pk=medicine_id)
# #     form = MedicineInventoryForm(request.POST or None, instance=obj)
# #     if form.is_valid():
# #         obj = form.save(commit=False)
# #         obj.save()
# #         messages.success("Successfully Updated")
# #         context = {'form' : form}
# #         return render(request,"update.html", context)
# #     else :
# #         context = {'form' : form, 'error' : "Not Updated"}
# #         return render(request,"update.html", context)


from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from medicineinventory.models import medicineinventory

class MedicineinventoryList(ListView):
    model = medicineinventory

class MedicineinventoryView(DetailView):
    model = medicineinventory

class MedicineinventoryCreate(CreateView):
    model = medicineinventory
    fields = ['medicine_id', 'medicine_name', 'medicine_groups', 'quantity_on_hand', 'reorder_level', 'reorder_quantity', 'medicine_price', 'supplier_id']
    success_url = reverse_lazy('medicineinventory_list')

class MedicineinventoryUpdate(UpdateView):
    model = medicineinventory
    fields = ['medicine_id', 'medicine_name', 'medicine_groups', 'quantity_on_hand', 'reorder_level', 'reorder_quantity', 'medicine_price', 'supplier_id']
    success_url = reverse_lazy('medicineinventory_list')

class MedicineinventoryDelete(DeleteView):
    model = medicineinventory
    success_url = reverse_lazy('medicineinventory_list')



def update(request) :
    i=1
    n=0
    famt = 0
    global context
    global mqty
    obj = []

    if request.method == 'POST' :
        data = json.loads(request.body) #dictionary
        
        for item in data['items']:
            medicine = medicineinventory.objects.get(medicine_id=item['medicine_id'])
            medicine.quantity_on_hand -= int(item['quantity'])
            medicine.save()
            n = (int(item['quantity']) * medicine.medicine_price * (medicine.medicine_groups.medicine_tax/100))
            total = medicine.medicine_price + n
            famt += total

            obj.append({'medicine': medicine, 'quantity': int(item['quantity']), 'price' : total})

    

    d = datetime.now()
    
    if(i<10) :
        bno = "BNO0{}".format(i)
    else :
        bno = "BNO{}".format(i)
    
    context = {
            'object' : obj,
            'date' : d,
            'billno' : bno,
            'finalamount' : famt,
    }

    return render(request,"createbill.html",context)
