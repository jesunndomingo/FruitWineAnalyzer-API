from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class update_table(models.Model):
    ph = models.CharField(max_length = 250)
    alcohol_content = models.CharField(max_length = 250)
    temperature = models.CharField(max_length = 250)
    volatile_acid = models.CharField(max_length = 250)
    uploaded = models.DateTimeField(default = datetime.datetime.now())
    rating = models.CharField(max_length = 250, blank = True)
   
   
  

    def __str__(self):
        return str(self.id)

class history_table(models.Model):
    ph = models.CharField(max_length = 250)
    alcohol_content = models.CharField(max_length = 250)
    temperature = models.CharField(max_length = 250)
    volatile_acid = models.CharField(max_length = 250)
    uploaded = models.DateTimeField(default = datetime.datetime.now())
    rating = models.CharField(max_length = 250, blank = True)
 


    def __str__(self):
        return str(self.id)