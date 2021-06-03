from django.db import models


# Create your models here.
class Person(models.Model):
    # definition of columns
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=8)
    email = models.EmailField()

    def __str__(self):
        return self.username
