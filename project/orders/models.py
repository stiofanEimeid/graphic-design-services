from django.db import models
from django.utils import timezone
from .choices import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.storage import default_storage as storage
from PIL import Image


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
    description     = models.TextField(blank=False, null=False)
    time_created    = models.DateTimeField(default=timezone.now)
    order_stage     = models.CharField(max_length=120, choices=DESIGN_STAGES, default="Design pending approval")
    order_number    = models.ForeignKey(Order, on_delete=models.CASCADE) #from where and what happens when deleted?

    def __str__(self):
        return self.customer

    def save(self, *args, **kwargs):
        super(Design, self).save(*args, **kwargs)
        if self.preview_image:
            image = Image.open(self.preview_image)
            if image.height > 300 or image.width > 300:
                    size = (300, 300)
                    image = Image.open(self.image)
                    image.thumbnail(size, Image.ANTIALIAS) 
                    fh = storage.open(self.image.name, "w")
                    format = 'png' 
                    image.save(fh, format)
                    fh.close()

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