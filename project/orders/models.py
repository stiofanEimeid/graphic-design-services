from django.db import models
from django.utils import timezone
from .choices import *
    
# Create your models here.
class Order(models.Model):
    type            = models.CharField(max_length=120, choices=ORDER_CHOICES, default='Logo')
    description     = models.TextField(blank=False, null=False)
    time_created    = models.DateTimeField(default=timezone.now)