from django.shortcuts import render

def home(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    return render(request, "home.html", {})
    
def gallery(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    return render(request, "gallery.html", {})
    
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
