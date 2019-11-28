# from django.shortcuts import render
# from .models import supplier
# from .forms import SupplierForm
# # Create your views here.
# def supplier_detail_view(request):
#     obj = supplier.objects.all()
#     context = {
#         'object' : obj
#     }
#     return render(request,"supplier/detail.html", context)

# def supplier_add_view(request):
#     form = SupplierForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = SupplierForm()
#     context = {
#         'form' : form
#     }
#     return render(request,"add.html", context)

from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from supplier.models import supplier

class SupplierList(ListView):
    model = supplier

class SupplierView(DetailView):
    model = supplier

class SupplierCreate(CreateView):
    model = supplier
    fields = ['supplier_id', 'supplier_name', 'supplier_address', 'supplier_contactno', 'supplier_email_id']
    success_url = reverse_lazy('supplier_list')

class SupplierUpdate(UpdateView):
    model = supplier
    fields = ['supplier_id', 'supplier_name', 'supplier_address', 'supplier_contactno', 'supplier_email_id']
    success_url = reverse_lazy('supplier_list')

class SupplierDelete(DeleteView):
    model = supplier
    success_url = reverse_lazy('supplier_list')