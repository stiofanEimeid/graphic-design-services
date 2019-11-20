from django.db import models
from django.utils import timezone
from .choices import *
from django.contrib.auth.models import User
from django.urls import reverse
    
# Create your models here.
class Order(models.Model):
    type            = models.CharField(max_length=120, choices=ORDER_CHOICES, default='Logo')
    description     = models.TextField(blank=False, null=False)
    time_created    = models.DateTimeField(default=timezone.now)
    customer        = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('order-detail', kwargs={'pk': self.pk})