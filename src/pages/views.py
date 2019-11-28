from django.shortcuts import render
from django.http import HttpResponse
def home_view(request,*args, **kwargs):
    # return HttpResponse("<H1> <center> Welcome To ViVa Pharmacy </H1>")
    return render(request,"home.html")
