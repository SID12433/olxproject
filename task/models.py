from django.db import models

# Create your models here.

class Vehicles(models.Model):
    name=models.CharField(max_length=200)
    owner=models.CharField(max_length=200)
    fuel_type=models.CharField(max_length=200)
    kilometre=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    location=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images",null=True)
    
    def _str_(self):
        return self.name
    
    


