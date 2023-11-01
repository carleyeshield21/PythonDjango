from django.db import models

# Create your models here.
class Forma(models.Model): #designing a database model
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    trabaho = models.CharField(max_length=80)
