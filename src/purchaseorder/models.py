from django.db import models
from supplier.models import supplier
class purchaseorder(models.Model) :
    purchase_orderno = models.CharField(max_length=10, default='PURNO',primary_key=True)
    purchase_orderdate = models.DateField(auto_now=True)
    shipment_address = models.CharField(max_length=100,default='Enter shipment address')
    supplier_id = models.ForeignKey(supplier,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.purchase_orderno)
        return str(self.supplier_id.supplier_name)
# Create your models here.
