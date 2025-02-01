from django.db import models
from django.contrib.auth.models import AbstractUser

from bank.models import AccType

# Create your models here.

class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=255, default='')
    birth_date = models.DateField(null=True, blank=True)
    currentBalance = models.DecimalField(max_digits=100, decimal_places=2,default=0.00)
    accType = models.ForeignKey(AccType, on_delete=models.PROTECT,null=True, blank=True)


class Transaction(models.Model):
    date = models.DateField()
    time = models.TimeField(auto_now_add=True)
    activity = models.CharField(max_length=100, null=True, blank=True)
    amount = models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    updatedBy = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=True, null=True)