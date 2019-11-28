from django.db import models
from medicineinventory.models import medicineinventory
from purchaseorder.models import purchaseorder
class purchase_detail(models.Model) :
    purchase_orderno = models.ForeignKey(purchaseorder,on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(medicineinventory,on_delete=models.CASCADE)
    unit_quantity = models.PositiveIntegerField(default = '1')
    additional_tax = models.DecimalField(max_digits=50,decimal_places=2, default='00.00')
    total_purchase_amount = models.DecimalField(max_digits=10000,decimal_places=2, default='00000.00')

    def __str__(self):
        return str(self.purchase_orderno)
        return str(self.medicine_id.medicine_name)
# Create your models here.
