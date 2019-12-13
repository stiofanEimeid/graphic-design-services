from django.shortcuts import render, redirect, reverse
from orders.forms import OrderForm

def view_basket(request):
    """A view that renders the content of the basket"""
    # if request.session['my_basket'] != None:
    context = {
            'type': request.session['my_basket']['type'],
            'description': request.session['my_basket']['description'],
            'price': request.session['my_basket']['price']
        }
    # else:
    #     context = {}
    return render(request, "basket.html", context)
    
# def add_to_basket(request):
#     """Add an order to the basket before proceeding to checkout"""
#     form = OrderForm(request.POST or None)
#     if form.is_valid():
        
#         customer    = request.user
#         type        = request.POST.get('type')
#         description = request.POST.get('description')
#         price       = 100
        
    
#         basket = request.session.get('basket', {})
#         basket[customer] = customer
#         basket[type] = type
#         basket[description] = description
#         basket[price] = price
        
#         form.save(commit=False)
#         return redirect(reverse('index'))
              
#     context = {
#         'form': form
#     }
#     return render(request, 'orders/create-order.html',  context)
    

