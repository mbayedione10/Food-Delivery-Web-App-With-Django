from django.urls import path
from restaurant.views import *

urlpatterns = [
            path('dashboard/', Dashboard.as_view(), name = 'dashboard'),
            path('order/<int:pk>/', OrderDetails.as_view(), name = 'order-details'),
            
            ]