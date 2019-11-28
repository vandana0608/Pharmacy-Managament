from django.shortcuts import render
from .models import bill_medicine
from .forms import BillMedicineForm
def bill_medicine_detail_view(request):
    obj = bill_medicine.objects.all()
    context = {
        'object' : obj
    }
    return render(request,"bill/detail.html", context)

# def billmedicine_add_view(request):
#     form = BillMedicineForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = BillMedicineForm()
#     context = {
#         'form' : form
#     }
#     return render(request,"add.html", context)


# import json
# import logging
# from json.decoder import JSONDecodeError
# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from .models import bill_medicine
# from .models import medicineinventory
# from datetime import datetime
# def bill_medicine_detail_view(request):
#     obj = bill_medicine.objects.all()
#     context = {
#         'object' : obj
#     }
#     return render(request,"bill/detail.html", context)

# def generate_bill(request):
#     logging.debug("in genearte bill view")
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         post = bill_medicine()
#         customername = data.customer_name
#         doctorname = data.doctor_name
#         billdate = datetime.now()
#         billno = '1BNO0'
#         bill_amount = 0


#         for item in data.items:
#             medicine_id = item.medicine_id
#             medicine = medicineinventory.objects.filter(medicine_id = medicine_id)
#             medicine_price = medicine.medicine_price
#             quantity = item.quantity
#             net_amount = medicine_price * quantity
#             bill_amount = bill_amount + net_amount
#             post.bill_no.bill_no = request.POST.get(billno)
#             post.medicine_id = request.POST.get(medicine_id)
#             post.quantity = request.POST.get(quantity)
#             post.net_amount = request.POST.get(net_amount)
#             post.amount = request.POST.get(bill_amount)
#             post.save()
#             # Insert bill_no, medicine_id, quantity, net_amount, amount into bill_medicine
#             # bill_amount = bill_amount + amount

#         post.bill_no.bill_date = request.POST.get(billdate)
#         post.bill_no.bill_no.customer_name = request.POST.get(customername)
#         post.bill_no.bill_no.doctor_name = request.POST.get(doctorname)
#         post.bill_no.bill_no.bill_amount = request.POST.get(bill_amount)
#         # Insert customer_name, doctor_name, bill_date, bill_amount, bill_no
#         return render(request,"createbill.html")

#     return render(request,"createbill.html")

