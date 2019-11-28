from django.db import models
from medicineinventory.models import medicineinventory
from bills.models import bill
class bill_medicine(models.Model) :
    #bill_no = models.CharField(max_length=10, default='BNO', primary_key=True)
    bill_no = models.ForeignKey(bill,on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(medicineinventory,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default='1')
    net_amount = models.DecimalField(max_digits=1000,decimal_places=2, default='0000.00')
    amount = models.DecimalField(max_digits=10000,decimal_places=2, default='00000.00')
    def __str__(self):
        return str(self.bill_no.bill_no)
        return str(self.medicine_id.medicine_name)
# Create your models here.
