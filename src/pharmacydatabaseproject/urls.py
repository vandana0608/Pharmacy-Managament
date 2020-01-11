"""pharmacydatabaseproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path , include
from django.views.generic.base import TemplateView 
from django.conf import settings
from django.conf.urls.static import static
from invoice_medicine.views import invoice_medicine_detail_view , invoicemedicine_add_view
from medicineinventory.views import medicineinventory_detail_view , update
from bill_medicine.views import bill_medicine_detail_view
from bills.views import bill_add_view , createb
from purchase_detail.views import purchase_detail_view , pod_add_view
from payment.views import payment_detail_view , payment_add_view
#from supplier.views import supplier_detail_view , supplier_add_view
from pages.views import home_view
from medicine_group.views import medicinegroup_add_view
from invoice.views import invoice_add_view
from purchaseorder.views import po_add_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
    path('',include('django.contrib.auth.urls')),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', TemplateView.as_view(template_name='invoice.html'), name='invoice'),
    path('', TemplateView.as_view(template_name='bill.html'), name='bill'),
    path('', TemplateView.as_view(template_name='medicineinventory.html'), name='medicineinventory'),
    path('', TemplateView.as_view(template_name='purchaseorder.html'), name='purchaseorder'),
    path('', TemplateView.as_view(template_name='payment.html'), name='payment'),
    path('', TemplateView.as_view(template_name='supplier.html'), name='supplier'),

    path('bill/',bill_medicine_detail_view,name='bill'),
    path('medicine/update/',update),

    path('createbill/',createb),

    # path('')

    #path('addmedicine/',medicineinventory_add_view,name='addmedicine'),
    path('addmedicinegroup/',medicinegroup_add_view,name='addmedicinegroup'),
    #path('addsupplier/',supplier_add_view,name='addsupplier'),
    path('addinvoice/',invoice_add_view,name='addinvoice'),
    path('addinvoicemedicine/',invoicemedicine_add_view,name='addinvoicemedicine'),
    path('addbill/',bill_add_view,name='addbill'),
    #path('addbillmedicine/',billmedicine_add_view,name='addbillmedicine'),
    #path('addbillmedicine/',billmedicine_add_view,name='addbillmedicine'),
    path('addpayment/',payment_add_view,name='addpayment'),
    path('addpurchaseorder/',po_add_view,name='addpurchaseorder'),
    path('addpurchaseorderdetails/',pod_add_view,name='addpurchaseorderdetails'),

    path('medicineinventory/',include('medicineinventory.urls')),
    path('supplier/', include('supplier.urls')),
    
    path('invoice/',invoice_medicine_detail_view,name='invoice'),
    path('medicine/',medicineinventory_detail_view,name='medicine'),
    path('purchaseorder/',purchase_detail_view,name='purchaseorder'),
    path('payment/',payment_detail_view,name='payment'),
    #path('supplier/',supplier_detail_view,name='supplier'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
