from django import forms
from .models import Order
from .choices import *

class OrderForm(forms.ModelForm):
    
    type        = forms.ChoiceField(choices = ORDER_CHOICES,
                                widget=forms.RadioSelect(attrs={"id": "type", "name": "description", "onclick":"calculateTotal()"}),
                                required=True)
                                
                                # initial='',
    description = forms.CharField(widget=forms.Textarea(attrs={"id": "description", "name": "description"}))
    
    class Meta:
        model = Order
        fields = [
            'type',
            'description',
            ]