from django.db import models
class Surgeries(models.Model):
    organ= models.CharField(max_length=100)
    price= price = models.FloatField()
    legal_age= models.BooleanField(default=True)
    def __str__(self):
        return self.organ
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
