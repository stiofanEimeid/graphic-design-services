from django import forms
from .models import Order, Design, Revision
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
            
class DesignSubmissionForm(forms.ModelForm):
    
    class Meta:
        model = Design
        fields = [
            'source_code',
            'preview_image',
            ]
            
class DesignUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Design
        fields = [
            'source_code',
            'preview_image',
            ]
            
class RevisionsForm(forms.ModelForm):
    
    class Meta:
        model = Revision
        fields = [
            'revisions',
            ]