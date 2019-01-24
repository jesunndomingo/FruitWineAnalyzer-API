from django.db import models
from django.utils import timezone
# Create your models here.

class fruitwine_table(models.Model):
    ph = models.CharField(max_length = 250)
    alcohol_content = models.CharField(max_length = 250)
    temperature = models.CharField(max_length = 250)
    volatile_acid = models.CharField(max_length = 250)

    def __str__(self):
        return str(self.id)