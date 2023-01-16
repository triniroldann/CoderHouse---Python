from django.db import models
class Doctors(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    birth_date = models.DateField(null=False, max_length=50)
    def __str__(self):
        return self.name
    
