from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    intro = models.TextField()
    description = models.TextField()
    specification = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField()
    location = models.CharField(max_length=50)
    stock = models.IntegerField()

    def __str__(self):
        return self.name +' - '+ str(self.stock)
        
    @property
    def line_total(self):
        return self.stock * self.price
