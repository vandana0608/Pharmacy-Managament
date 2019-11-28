from django.db import models
class medicine_group(models.Model) : 
    #medicine_groups = models.ForeignKey(medicineinventory,on_delete=models.CASCADE)
    medicine_groups = models.CharField(max_length=20, default='xxx',primary_key=True)
    medicine_tax = models.DecimalField(max_digits=50,decimal_places=2, default='00.00')
    tax_effective_date = models.DateField()
    def __str__(self):
        return str(self.medicine_groups)
# Create your models here.
