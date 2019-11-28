from django.db import models
from django.urls import reverse
from supplier.models import supplier
from medicine_group.models import medicine_group
class medicineinventory(models.Model) : 
        medicine_id = models.CharField(max_length=10, default='MID',primary_key=True)
        medicine_name = models.CharField(max_length=35, default='xxx')
        medicine_groups = models.ForeignKey(medicine_group,on_delete=models.CASCADE)
        quantity_on_hand = models.PositiveIntegerField(default = '0')
        reorder_level = models.PositiveIntegerField(default = '1')
        reorder_quantity = models.PositiveIntegerField(default = '1')
        medicine_price = models.DecimalField(max_digits=10000,decimal_places=2, default='00000.00')
        supplier_id = models.ForeignKey(supplier,on_delete=models.CASCADE)

        def __str__(self):
                return str(self.medicine_name)
                return str(self.medicine_groups.medicine_groups)
                return str(self.supplier_id.supplier_id)
        
        def get_absolute_url(self):
                return reverse('medicineinventory_edit', kwargs={'pk': self.pk})

# Create your models here.
