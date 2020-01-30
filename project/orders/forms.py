from django import forms
from .models import Order, Design, Revision, Testimonial
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
            'reference',
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
            
class DesignAcceptanceForm(forms.ModelForm):
    
    class Meta:
        model = Design
        fields = [
            'order_stage'
        ]
        
class RevisionsForm(forms.ModelForm):
    
    class Meta:
        model = Revision
        fields = [
            'revisions',
            ]

class TestimonialForm(forms.ModelForm):
    
    class Meta:
        model = Testimonial
        fields = [
            'testimonial_text'
            ]