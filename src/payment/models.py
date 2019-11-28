from django.db import models
from supplier.models import supplier
from purchaseorder.models import purchaseorder
class payment(models.Model) :
    payment_id = models.CharField(max_length=10, default='PYID',primary_key=True)
    payment_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=10000,decimal_places=2, default='00000.00')
    payment_details = models.CharField(max_length=25,default='Cheque/DD/NEFT')
    purchase_orderno = models.ForeignKey(purchaseorder,on_delete=models.CASCADE)
    supplier_id = models.ForeignKey(supplier,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.payment_id)
        return str(self.purchase_orderno)
        return str(self.supplier_id.supplier_name)
    
# Create your models here.
