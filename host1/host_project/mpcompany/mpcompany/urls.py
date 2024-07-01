"""
URL configuration for mpcompany project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from mp_app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('about',views.about),
    path('contact',views.contact),
    path('portfolio',views.portfolio),
    path('service',views.service),
    path('Registration', views.Registration),
    path('login', views.login),
    path('adminhome', views.adminhome),
    path('userhome', views.userhome),
    path('about_1', views.about_1),
    path('contactas_1', views.contactas_1),
    path('portfolio_1', views.portfolio_1),
    path('services_1', views.services_1),
    path('addevents', views.addevents),
    path('bookingdetails', views.bookingdetails),
    path('userdetails', views.userdetails),
    path('contactdetails', views.contactdetails),
    path('logout',views.logout),
    path('photos',views.photos),
    path('videos',views.videos),
    path('form/<int:d>/<int:amt>',views.form),
    path('payment/<int:amt>',views.payment),
    path('payment',views.payment),
    path('profile',views.profile),
    path('updateprofile',views.updateprofile),
    path('delete/<int:d>',views.delete_event),
    path('forgot',views.forgot_password),
    path('booking_details',views.booking1),
    path('manageevent',views.manageevent),
    path('success_1',views.success_2),
    path('reset/<token>',views.reset_password),
    path('update/<int:d>',views.updateevent),
    path('delete/<int:d>',views.delete_product),
    # path('payment_callback/', views.payment_callback, name='payment_callback'),


]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
