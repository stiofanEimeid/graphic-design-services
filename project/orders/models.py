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
    price           = models.DecimalField(decimal_places=2, max_digits=1000)
    open            = models.BooleanField(default=True)
    
    # def __str__(self):
    #     return self.type

    def get_absolute_url(self):
        return reverse('order-detail', kwargs={'pk': self.pk})
        
class Design(models.Model):
    
    source_code     = models.FileField(upload_to='designs') 
    preview_image   = models.ImageField(upload_to='preview_images')
    customer        = models.CharField(max_length=120)
    type            = models.CharField(max_length=120)
    time_created    = models.DateTimeField(default=timezone.now)
    order_stage     = models.CharField(max_length=120, choices=DESIGN_STAGES, default="Design pending approval")
    order_number    = models.ForeignKey(Order, on_delete=models.CASCADE) #from where and what happens when deleted?
    
    def __str__(self):
        return self.customer
        
class Revision(models.Model):

    design_id       = models.ForeignKey(Design, on_delete=models.CASCADE) #from where and what happens when deleted?
    customer        = models.CharField(max_length=120)
    type            = models.CharField(max_length=120)
    revisions       = models.TextField(blank=False, null=False)
    time_created    = models.DateTimeField(default=timezone.now)
    price           = models.DecimalField(decimal_places=2, max_digits=1000)
    open            = models.BooleanField(default=True)
   
    def __str__(self):
        return self.customer
        
    
    