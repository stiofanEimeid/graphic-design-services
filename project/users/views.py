from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from orders.models import Order, Design

# CoreySchafer Code Begins

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request, *args, **kwargs):
    if request.method == 'POST':
        """determine nature of the request and display the appropriate content"""
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'orders': Order.objects.filter(customer=request.user),
        'designs': Design.objects.filter(customer=request.user),
        """Add count of designs awaiting approval to template to
        better allow the user to see when they are available"""
        'newdesigns': Design.objects.filter(customer=request.user, order_stage="Design pending approval").count()
    }
    return render(request, 'profile.html', context)

# CoreySchafer Code Ends