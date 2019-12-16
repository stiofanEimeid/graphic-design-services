from django.shortcuts import render
from .forms import OrderForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Order

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# class OrderCreateView(LoginRequiredMixin, CreateView):
#     template_name = "orders/create_order.html"
    
#     form_class = OrderForm
        
#     def form_valid(self, form):
#         form.instance.customer = self.request.user
#         form.instance.price = 100
#         return super().form_valid(form)
        
 
        
# @login_required
# def order_create_view(request):
#     form = OrderForm(request.POST or None)
#     if form.is_valid():
#         form.instance.customer = request.user
#         # form.instance.customer = price
#         form.save()
#         form = OrderForm()
        
        
#     context = {
#         'form': form
#     }
#     return render(request, 'orders/create_order.html',  context)

# @login_required
# def order_create_view(request):
#     form = OrderForm(request.POST or None)
#     if form.is_valid():
#         form.instance.customer = request.user
#         form.instance.price = 100
#         content = form.save(commit=False)
        
#         context = {
#             'content' : content
#         }
#         return render(request, 'orders/preview_order.html', context)
        
#     context = {
#         'form': form
#     }
#     return render(request, 'orders/create_order.html',  context)
    
@login_required
def order_create_view(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        """Create a dictionary 'basket' that stores order info"""
        my_basket = request.session.get('my_basket', {})
        request.session['my_basket'] = my_basket
        request.session['my_basket']['type'] = request.POST.get('type')
        request.session['my_basket']['description'] = request.POST.get('description')
        
        """Calculate cost of order"""
        request.session['my_basket']['price'] = '100'
        
        # request.session.modified = True
        """add dictionary to session variable 'basket'"""
        # request.session['basket'] = basket
       
        context = {
            'type': request.session['my_basket']['type'],
            'description': request.session['my_basket']['description'],
            'price': request.session['my_basket']['price']
        }
       
        return render(request, 'basket.html', context)
        
    context = {
        'form': form
    }
    return render(request, 'orders/create_order.html',  context)
    

def save_order(request):
    
    return render(request, 'home.html')
    
    


# @staff_member_required    
# def order_list(request):
#     orders = Order.objects.all()
#     return render(request, 'orders/order_list.html', {"orders": orders})

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "order_list.html"
    context_object_name = 'orders'
    ordering = ['-time_created']


# Must make accessible to respective owners and admin only
class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order