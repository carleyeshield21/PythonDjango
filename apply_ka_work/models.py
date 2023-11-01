from django.db import models

# Create your models here.
class Forma(models.Model): #designing a database model, model for database
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    trabaho = models.CharField(max_length=80)

    def __str__(self): #this method will display the string representation of the object, without this funtion the display will be an object that
        # is not readable by humans
        return f'{self.firstname} {self.lastname}'
