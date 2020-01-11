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

from django.shortcuts import render,redirect
from .models import bill
import json

def createb(request) :
    if request.method == 'POST' :
        data = json.loads(request.body) #dictionary
        
        for item in data['items']:
            bill_no = item['billno']
            bill_date = item['date']
            bill_final_amount = item['finalamount']
            bill.save(bill_no,bill_date,bill_final_amount)

    return render(request,"medicine\detail.html",context)