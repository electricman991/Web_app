from django.db import models

# Create your models here.

class Workers(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    salary = models.FloatField()
    time = models.DateTimeField('date added')
    def __str__(self):
        return self.name + self.address + self.phone + self.email 
    
    def __float__(self):
        return self.salary




