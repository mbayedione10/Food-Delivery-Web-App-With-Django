from django.shortcuts import render

# Create your views here.
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import datetime
from customer.models import OrderModel


class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        #get the current date
        today = datetime.today()
        orders = OrderModel.objects.all()
            #created_on__year=today.year,created_on__month=today.month,created_on__day=today.day)
        #Loop through the orders and add the price value and check if order is not shipped

        unshipped_order = []
        total_revenue = 0
        for order in orders:
            total_revenue += order.price
            if not order.is_shipped:
                unshipped_order.append(order)



        #Pass total number orders and total revenue into template
        context={
            'orders': unshipped_order,
            'total_revenue': total_revenue,
            'total_orders': len(orders)
        }

        return render(request,'restaurant/dashboard.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff') 

class OrderDetails(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        context = {'order': order}

        return render(request, 'restaurant/order-details.html', context)
    
    def post(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        order.is_shipped = True
        order.is_paid = True

        order.save()
        
        context = {'order': order}
        return render(request, 'restaurant/order-details.html', context)

    
    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()