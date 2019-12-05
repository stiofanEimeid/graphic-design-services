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

from pages.views import home, gallery, pricing, orders, showcase
from users import views as user_views
from orders import views as order_views
from orders.views import Order, OrderDetailView, OrderCreateView, OrderListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="homepage"),
    path("gallery/", gallery, name="gallery"),
    path("pricing/", pricing, name="pricing"),
    path("orders/", orders, name="orders"),
    path("showcase/", showcase, name="showcase"),
    path('register/', user_views.register, name='register'),
    # path('create-order/', order_views.order_create_view, name='create-order'),
    path('create-order/', OrderCreateView.as_view(), name='create-order'),
    # path('order-list/', order_views.order_list, name='order-list'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)