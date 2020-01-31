from django.db import models
from django.utils import timezone
from .choices import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.storage import default_storage as storage

class Order(models.Model):
    type            = models.CharField(max_length=120, choices=ORDER_CHOICES, default='Logo')
    description     = models.TextField(blank=False, null=False)
    time_created    = models.DateTimeField(default=timezone.now)
    customer        = models.ForeignKey(User, on_delete=models.CASCADE)
    price           = models.DecimalField(decimal_places=2, max_digits=1000)
    open            = models.BooleanField(default=True)
    reference       = models.FileField(upload_to='references', blank=True)

    # def __str__(self):
    #     return self.type

    def get_absolute_url(self):
        return reverse('order-detail', kwargs={'pk': self.pk})

class Design(models.Model):

    sub_design      = models.FileField(upload_to='designs') 
    customer        = models.CharField(max_length=120)
    type            = models.CharField(max_length=120)
    description     = models.TextField(blank=False, null=False)
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

    # def __str__(self):
    #     return self.customer
    def get_absolute_url(self):
        return reverse('revision-detail', kwargs={'pk': self.pk})


class Testimonial(models.Model):
    design_id           = models.ForeignKey(Design, on_delete=models.CASCADE)
    customer            = models.CharField(max_length=120)
    time_created        = models.DateTimeField(default=timezone.now)
    testimonial_text    = models.TextField(blank=False, null=False)
    
    def __str__(self):
        return self.customer