# from django.urls import path
# from django.conf.urls  import url, include
# from . import views
# from django.conf import settings

from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
#from customer.views import Index, About
from customer.views import *


urlpatterns = [
    path('', Index.as_view(), name = 'index'),
    path('about/', About.as_view(), name = 'about'),
    path('order/', Order.as_view(), name = 'order'),
    path('order-confrmation/<int:pk>', OrderConfirmation1.as_view(), name = 'order-confirmation'),
    path('payment_confirmation/', OrderPayConfirmation.as_view(), name = 'payment-submitted'),
    path('menu/', Menu.as_view(), name= 'menu'),
    path('menu/search', MenuSearch.as_view(), name='menu-search'),


]