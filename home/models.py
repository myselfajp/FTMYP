from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50,default='')
    email = models.CharField(max_length=150,default='')
    message = models.TextField(default='')

    def __str__(self):
        return self.name
