from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vehicles(models.Model):
    name=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fuel_type=models.CharField(max_length=200)
    kilometre=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    location=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images",null=True)
    
    def _str_(self):
        return self.name
    
    


