from django.shortcuts import render
from .models import payment
from .forms import PaymentForm
def payment_detail_view(request):
    obj = payment.objects.all()
    context = {
        'object' : obj
    }
    return render(request,"payment/detail.html", context)

def payment_add_view(request):
    form = PaymentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PaymentForm()
    context = {
        'form' : form
    }
    return render(request,"add.html", context)
# Create your views here.
