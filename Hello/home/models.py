from django.db import models

# Create your models here.

class contact(models.model):
    name = models.charfeild(max_length=122)
    email = models.charfeild(max_length=122)
    phone = models.charfeild(max_length=12)
    desc = models.TextField()
    date = models.DateField()