from django import forms
from .models import Order
from .choices import *

class OrderForm(forms.ModelForm):
    
    type        = forms.ChoiceField(choices = ORDER_CHOICES, label="", initial='',
                                widget=forms.Select(attrs={"id": "type"}),
                                required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={"id": "description"}))
    
    class Meta:
        model = Order
        fields = [
            'type',
            'description',
            ]