from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    img = models.ImageField()
    def __str__(self):
           return self.description
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    img = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
 
    def __str__(self):
           return self.description



