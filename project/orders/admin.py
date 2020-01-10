from django.contrib import admin
from .models import Order, Design

# Register your models here.
admin.site.register([Order, Design])