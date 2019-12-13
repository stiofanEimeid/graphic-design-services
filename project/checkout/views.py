from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, CustomerDetailForm
from orders.models import Order
from django.conf import settings
from django.utils import timezone
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method=="POST":
        cd_form = CustomerDetailForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if cd_form.is_valid() and payment_form.is_valid():
            customer_details = cd_form.save(commit=False)
            customer_details.date = timezone.now()
            customer_details.save()
            
            """get session variables for order"""
            # is this the right place for this? only add when payment is successful?
            order = Order(
                type = request.session['my_basket']['type'],
                description = request.session['my_basket']['description'],
                customer = request.user,
                price = request.session['my_basket']['price'],
                time_created = timezone.now()
                )
        
            order.save()
            
            try:
                    customer = stripe.Charge.create(
                    amount = int(request.session['my_basket']['price'] * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['basket'] = {}
                return redirect(reverse('homepage'))
            else:
                messages.error(request, "Unable to receive payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        cd_form = CustomerDetailForm()
        
    return render(request, "checkout.html", {
            'cd_form': cd_form, 
            'payment_form': payment_form,
            'publishable': settings.STRIPE_PUBLISHABLE,
            'type': request.session['my_basket']['type'],
            'description': request.session['my_basket']['description'],
            })
