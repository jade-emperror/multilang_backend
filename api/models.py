from django.db import models

# Create your models here.
class Product(models.Model):
    prod_id=models.AutoField(primary_key=True)
    prod_name_en=models.CharField(max_length=50)
    prod_desc_en=models.CharField(max_length=75)
    prod_class_en=models.CharField(max_length=75)
    prod_name_ta=models.CharField(max_length=50)
    prod_desc_ta=models.CharField(max_length=75)
    prod_class_ta=models.CharField(max_length=75)
    prod_name_ka=models.CharField(max_length=50)
    prod_desc_ka=models.CharField(max_length=75)
    prod_class_ka=models.CharField(max_length=75)