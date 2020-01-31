from django.shortcuts import render, redirect, reverse
from orders.forms import OrderForm


def view_basket(request):
    """A view that renders the content of the basket"""
    return render(request, "basket.html", {})

    

