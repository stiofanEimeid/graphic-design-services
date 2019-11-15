from django.db import models

# Create your models here.
class Order(models.Model):
    type        = models.CharField(max_length=120)
    description = models.TextField(blank=False, null=False)