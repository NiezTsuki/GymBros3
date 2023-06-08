from django.db import models

# Create your models here.

class producto(models.Model):
    id     =models.CharField(primary_key=True, max_length=10)
    nombre =models.CharField(max_length=20)
    desc   =models.CharField(max_length=200)
    precio =models.CharField(max_length=10)

