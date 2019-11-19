from django.shortcuts import render
from .forms import OrderForm
from .models import Order

from django.contrib.auth.decorators import login_required

@login_required
def order_create_view(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = OrderForm()
    context = {
        'form': form
    }
    return render(request, 'create_order.html',  context)
    
# def order_list(request):
    # ...
    # return render(request, 'order_list.html', {})
