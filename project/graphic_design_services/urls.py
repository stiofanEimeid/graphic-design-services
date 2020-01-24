"""graphic_design_services URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from pages import views as page_views 
from users import views as user_views
from orders import views as order_views
from checkout.views import checkout
from basket.views import view_basket
from orders.views import Order, OrderDetailView, OrderListView, RevisionDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", page_views.home, name="homepage"),
    path("gallery/", page_views.gallery, name="gallery"),
    path("orders/", page_views.orders, name="orders"),
    path("gallery-design-detail/<int:parameter>/", page_views.gallery_design_detail, name="gallery_design_detail"),
    path('register/', user_views.register, name='register'),
    path('create-order/', order_views.order_create_view, name='create-order'),
    path('checkout/', checkout, name='checkout'),
    path("basket/", view_basket, name="basket"),
    path('submit-design/<int:parameter>/', order_views.submit_design, name='submit-design'),
    path('request-changes/<int:parameter>/', order_views.request_changes, name='request-changes'),
    path('design-detail/<int:parameter>/', order_views.design_detail, name='design-detail'),
    path('submit-revision/<int:parameter>/', order_views.submit_revision, name='submit-revision'),
    path('testimonial/<int:parameter>/', order_views.testimonial, name='testimonial'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('revision/<int:pk>/', RevisionDetailView.as_view(), name='revision-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password-reset/', 
          auth_views.PasswordResetView.as_view(
          template_name='password_reset.html'),
          name='password_reset'),
    path('password-reset/done', 
          auth_views.PasswordResetDoneView.as_view(
          template_name='password_reset_done.html'),
          name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
          auth_views.PasswordResetConfirmView.as_view(
          template_name='password_reset_confirm.html'),
          name='password_reset_confirm'),
    path('password-reset-complete/', 
          auth_views.PasswordResetCompleteView.as_view(
          template_name='password_reset_complete.html'),
          name='password_reset_complete'),
    
    path('profile/', user_views.profile, name='profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)