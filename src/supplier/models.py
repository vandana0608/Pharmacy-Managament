from django.db import models
from django.urls import reverse
class supplier(models.Model) :
    supplier_id = models.CharField(max_length=10, default='SID',primary_key=True)
    supplier_name = models.CharField(max_length=25, default='xxx')
    supplier_address = models.CharField(max_length=30, default='xxx')
    supplier_contactno = models.CharField(max_length=12,default='080-')
    supplier_email_id = models.CharField(max_length=35, default='xxxxx@xxxxx.com')

    def __str__(self):
        return str(self.supplier_name)
    
    def get_absolute_url(self):
        return reverse('supplier_edit', kwargs={'pk': self.pk})
# Create your models here.
