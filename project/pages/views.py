from django.shortcuts import render, render_to_response
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from orders.models import Design, Testimonial


def home(request, *args, **kwargs):
    """A view for rendering the homepage"""
    return render(request, "home.html", {})

def gallery(request, *args, **kwargs):
    """A view for rendering the gallery"""
    illustrations = Design.objects.filter(order_stage="Design accepted", type="Illustration")
    logos= Design.objects.filter(order_stage="Design accepted", type="Logo")
    avatars = Design.objects.filter(order_stage="Design accepted", type="Avatar")
    icons = Design.objects.filter(order_stage="Design accepted", type="Icon")
    context = {
        "illustrations": illustrations,
        "logos": logos,
        "avatars": avatars,
        "icons": icons
    }
    return render(request, "gallery.html", context)


def gallery_design_detail(request, parameter):
    """A view for rendering individual gallery pages.
       Check if a testimonial has been added by the
       customer and render. Otherwise ignore."""
    try:
        testimonial = Testimonial.objects.get(design_id=parameter)
    except MultipleObjectsReturned:
        testimonial = Testimonial.objects.filter(design_id=parameter).last()
    except ObjectDoesNotExist:
        testimonial = None
    context = {
        "design": Design.objects.get(pk=parameter),
        "testimonial": testimonial
    }
    return render(request, "gallery_design_detail.html", context)


def orders(request, *args, **kwargs):
    return render(request, "orders.html", {})

"""Custom Handlers"""

def handler403(request, exception, template_name="403.html"):
    response = render_to_response("403.html")
    response.status_code = 403
    return response


def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response


def handler500(request, exception, template_name="500.html"):
    response = render_to_response("500.html")
    response.status_code = 500
    return response
