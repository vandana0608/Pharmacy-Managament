from django.db import models
from medicineinventory.models import medicineinventory
from invoice.models import invoice
class invoice_medicine(models.Model) :
    invoice_no = models.ForeignKey(invoice,on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(medicineinventory,on_delete=models.CASCADE)
    unit_quantity = models.PositiveIntegerField(default ='1')
    additional_tax = models.DecimalField(max_digits=50,decimal_places=2, default='00.00')
    total_amount = models.DecimalField(max_digits=1000,decimal_places=2, default='0000.00')

    def __str__(self):
        return str(self.invoice_no)
        return str(self.medicine_id.medicine_name)
# Create your models here.
