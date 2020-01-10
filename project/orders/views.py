from django.shortcuts import render, redirect
from .forms import OrderForm, DesignSubmissionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Order, Design

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
        
        selected_type = request.session['my_basket']['type']
   
        if selected_type == "Logo":
            request.session['my_basket']['price'] = 20
        elif selected_type == "Icon":
            request.session['my_basket']['price'] = 25
        elif selected_type == "Poster":
            request.session['my_basket']['price'] = 35
        else:
            request.session['my_basket']['price'] = 89
    
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
    
@login_required
def submit_design(request, parameter):
    getOrder = Order.objects.get(pk=parameter)
    if request.method == 'POST':
        
        form = DesignSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer = getOrder.customer
            instance.order_number = getOrder
            instance.save()
            # change order_status of order object
            return redirect('order-list')
    else:
        form = DesignSubmissionForm()
        
    return render(request, 'orders/submit_design.html', {"order": getOrder,'form': form})
    # getOrder = Order.objects.get(pk=parameter)
    # form = DesignSubmissionForm(request.POST or None)
    # if form.is_valid():
    #     instance = form.save(commit=False)
    #     instance.customer = getOrder.customer
    #     instance.order_number = parameter
    #     instance.save()
    #     # change order_status of order object
    #     return redirect('order-list')
        
    # context = {
    #     "order": getOrder,
    #     'form': form
    # }
    # return render(request, 'orders/submit_design.html', context)

@login_required
def testimonial(request, parameter):
    # make this a form
    
    
    context={
        'myvariable': parameter
    }
    return render(request, 'orders/testimonial.html', context)
    