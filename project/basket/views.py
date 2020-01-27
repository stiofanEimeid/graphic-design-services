from django.shortcuts import render, redirect, reverse
from orders.forms import OrderForm


def view_basket(request):
    """A view that renders the content of the basket"""
    context = {
            'type': request.session['my_basket']['type'],
            'description': request.session['my_basket']['description'],
            'price': request.session['my_basket']['price']
        }
    return render(request, "basket.html", context)

    

