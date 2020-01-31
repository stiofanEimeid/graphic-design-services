from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm, DesignSubmissionForm, DesignUpdateForm, RevisionsForm, DesignAcceptanceForm, TestimonialForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Order, Design, Revision
from django.core.exceptions import PermissionDenied

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


@login_required
def order_create_view(request, *args, **kwargs):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        """Create a dictionary 'basket' that stores order info"""
        my_basket = request.session.get('my_basket', {})
        request.session['my_basket'] = my_basket
        request.session['my_basket']['type'] = form.cleaned_data.get('type')
        request.session['my_basket']['description'] = form.cleaned_data.get('description')
        request.session['my_basket']['revision'] = False

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
    return render(request, 'create_order.html',  context)


class OrderListView(UserPassesTestMixin, ListView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Order
    template_name = "order_list.html"
    context_object_name = 'orders'
    ordering = ['-time_created']

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        context.update({
            'revisions': Revision.objects.order_by('-time_created'),
        })
        return context

    def get_queryset(self):
        return Order.objects.order_by('-time_created')


class OrderDetailView(UserPassesTestMixin, DetailView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Order
    template_name = "order_detail.html"


class RevisionDetailView(UserPassesTestMixin, DetailView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Revision
    template_name = "revision_detail.html"


def submit_design(request, parameter):
    if request.user.is_superuser:
        getOrder = Order.objects.get(pk=parameter)
        if request.method == 'POST':
    
            form = DesignSubmissionForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.customer = getOrder.customer
                # may not actually be necessary
                instance.type = getOrder.type
                instance.description = getOrder.description
                instance.order_number = getOrder
                instance.save()
                Order.objects.filter(pk=parameter).update(open=False)
                return redirect('order-list')
        else:
            form = DesignSubmissionForm()
    
        return render(request, 'submit_design.html', {"order": getOrder, 'form': form})
    return render(request, '403.html', {})


def submit_revision(request, parameter):
    if request.user.is_superuser:
        getRevision = Revision.objects.get(pk=parameter)
        getDesign = getRevision.design_id
        if request.method == 'POST':
    
            form = DesignUpdateForm(request.POST, request.FILES, instance=getDesign)
            if form.is_valid():
                form.save(commit=False)
                # Revision.objects.filter(pk=parameter).update(open=False)
                # Add revision.revisions to design array
                Design.objects.filter(pk=getDesign).update(order_status="Design pending approval")
                form.save()
    
                return redirect('order-list')
        else:
            form = DesignUpdateForm()
    
        return render(request, 'submit_revision.html', {'design': getDesign, 'revision': getRevision, 'form': form})
    return render(request, '403.html', {})


@login_required
def request_changes(request, parameter):
    form = RevisionsForm(request.POST or None)
    if form.is_valid():
        """Create a dictionary 'basket' that stores order info"""
        design = Design.objects.get(pk=parameter)
        # get parent
        order = Order.objects.get(pk=design.order_number.pk)
        my_basket = request.session.get('my_basket', {})
        request.session['my_basket'] = my_basket
        request.session['my_basket']['type'] = design.type
        request.session['my_basket']['description'] = form.cleaned_data.get('revisions')
        request.session['my_basket']['price'] = int(order.price) * 0.15
        request.session['my_basket']['design_id'] = parameter
        request.session['my_basket']['revision'] = True

        context = {
            'type': request.session['my_basket']['type'],
            'description': request.session['my_basket']['description'],
            'price': request.session['my_basket']['price']
        }

        return render(request, 'checkout.html', context)

    return render(request, 'request_changes.html', {"form": form,
                                                    'DesignNumber': parameter})


@login_required
def design_detail(request, parameter):
    # getDesign = get_object_or_404(Design, pk=parameter, customer=request.user)
    getDesign = Design.objects.get(pk=parameter)
    # designOwner = getattr(getDesign, 'customer')
    designOwner = getDesign.customer

    if request.user.username != designOwner:
        raise PermissionDenied

    if request.method == 'POST':
        if request.POST.get('status') == 'accept':
            Design.objects.filter(pk=parameter).update(order_stage="Design accepted")
        return redirect('profile')

    context = {
        'design': getDesign,
        'designrevisions': Revision.objects.filter(pk=getDesign.id).order_by(
                                                    '-time_created'),
    }
    return render(request, 'design_detail.html', context)


@login_required
def testimonial(request, parameter):
    form = TestimonialForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
        # Must return instance
        form.design = parameter
        form.customer = request.user
        form.save()

        return redirect('profile')
    context = {
        'form': form,
        'design': parameter
    }
    return render(request, 'testimonial.html', context)
