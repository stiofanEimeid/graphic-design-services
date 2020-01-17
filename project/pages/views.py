from django.shortcuts import render
from orders.models import Design

def home(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    return render(request, "home.html", {})
    
def gallery(request, *args, **kwargs):
    context ={
        "designs": Design.objects.filter(order_stage="Design accepted")
    }
    return render(request, "gallery.html", context)
    
def gallery_design_detail(request, parameter):
    
    return render(request, 'gallery_design_detail.html')
    
def showcase(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    return render(request, "showcase.html", {})

def pricing(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    return render(request, "pricing.html", {})
    
def orders(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    return render(request, "orders/orders.html", {})
