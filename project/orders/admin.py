from django.contrib import admin
from .models import Order, Design, Revision

# Register your models here.
admin.site.register([Order, Design, Revision])