from django.db import models
class bill(models.Model) :
    bill_no = models.CharField(max_length=10, default='BNO', primary_key=True)
    bill_date = models.DateField(auto_now=True)
    customer_name = models.CharField(max_length=15, default='xxx')
    doctor_name = models.CharField(max_length=35,default='Dr.xxx')
    bill_amount = models.DecimalField(max_digits=10000,decimal_places=2, default='00000.00')
    def __str__(self):
        return str(self.bill_no)
# Create your models here.
