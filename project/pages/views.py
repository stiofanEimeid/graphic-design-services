from django.shortcuts import render

def home(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    return render(request, "home.html", {})
    
def gallery(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    return render(request, "gallery.html", {})

def pricing(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    return render(request, "pricing.html", {})
