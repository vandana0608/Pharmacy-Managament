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
        billno = data['billno']
        billdate = data['date']
        billfinalamount = data['finalamount']
        bill.save(bill_no = billno, bill_date = billdate, bill_amount = billfinalamount)

    return render(request,"createbill.html")