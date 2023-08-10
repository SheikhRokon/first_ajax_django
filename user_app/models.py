from django.db import models

# Create your models here.

class Registration(models.Model):
    
    user_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField(max_length=14)
   

    def __str__(self):
        pass
