from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)

    def _str_(self):
        return self.text

class post(models.Model):
    url_name = models.CharField(max_length=40)
    url_link = models.CharField(max_length=40)
   
