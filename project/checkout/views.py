from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, CustomerDetailForm
from orders.models import Order, Revision, Design
from django.conf import settings
from django.utils import timezone
import stripe


stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    """A view to allow users to make purchases"""
    if request.method == "POST":
        cd_form = CustomerDetailForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if cd_form.is_valid() and payment_form.is_valid():
            customer_details = cd_form.save(commit=False)
            customer_details.date = timezone.now()
            customer_details.save()

            try:
                customer = stripe.Charge.create(
                                                amount=int(request.session['my_basket']['price'] * 100),
                                                currency="EUR",
                                                description=request.user.email,
                                                card=payment_form.cleaned_data['stripe_id'],
                                                 )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid")

                """Determine the nature of the order and save"""

                if request.session['my_basket']['revision'] is True:
                    Design.objects.filter(id=request.session['my_basket']['design_id']).update(order_stage='Revisions requested'),
                    revision = Revision(
                        design_id=Design.objects.get(id=request.session['my_basket']['design_id']),
                        revisions=request.session['my_basket']['description'],
                        author=request.user,
                        price=request.session['my_basket']['price'],
                        type=request.session['my_basket']['type'],
                        time_created=timezone.now()
                        )
                    revision.save()

                else:
                    """get session variables for order"""
                    order = Order(
                        type=request.session['my_basket']['type'],
                        description=request.session['my_basket']['description'],
                        author=request.user,
                        price=request.session['my_basket']['price'],
                        time_created=timezone.now()
                        )
                    order.save()
                    """The revision/design object is only saved if payment is successful"""

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
            'price': request.session['my_basket']['price'],
            })
