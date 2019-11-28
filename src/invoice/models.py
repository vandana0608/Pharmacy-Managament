from django.db import models
from supplier.models import supplier
#from datetime import datetime
class invoice(models.Model) :
    #date = models.DateField(auto_now_add=True)
    invoice_no = models.CharField(max_length=10, default='INVNO',primary_key=True)
    invoice_date = models.DateField()
    supplier_id = models.ForeignKey(supplier,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.invoice_no)
        return str(self.supplier_id.supplier_name)
# Create your models here.
