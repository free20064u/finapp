from django.db import models


# Create your models here.
class AccType(models.Model):
    accTypeName = models.CharField(max_length=100, verbose_name="Account Type", unique=True, default='')

    def __str__(self):
        return self.accTypeName





