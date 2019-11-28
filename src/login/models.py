from django.db import models
from datetime import datetime
class login(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    login = models.DateTimeField(default = datetime.now)
    logout = models.DateTimeField(default = datetime.now)
    username = models.CharField(max_length=10, default= 'admin')

    #def __str__(self):
        #return self.username

# Create your models here.
