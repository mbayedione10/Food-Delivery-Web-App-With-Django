from django.shortcuts import render, redirect
# Create your views here.
from django.views import View
from customer.models import *
from django.db.models import Q
from django.core.mail import send_mail
from rest_framework.response import Response
from customer.serializers import *


class Index(View):
    def get(self,request, *args, **kwargs):
        return render(request,'customer/index.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

class Order1(View):
    def get(self, request, *args, **kwargs):
        
          #Get every item from each category
        appetizers = MenuItem.objects.filter(category__name__contains='appetizer')
        entres = MenuItem.objects.filter(category__name__contains='Entre')
        desserts = MenuItem.objects.filter(category__name__contains='Dessert')
        drinks = MenuItem.objects.filter(category__name__contains='Drink')
          #pass into context
        context = {

              'appetizers': appetizers,
              'entres': entres,
              'desserts': desserts,
              'drinks': drinks
          }
          #render the template 
        return render(request, 'customer/order.html', context)


    def post(self, request, *args, **kwargs):
        """
        grab all the selected items
        get the menu item for that item that's seleected
        return the name,  price and id to figure out some calculations on the price 
        
        and return something lateer
        """
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        #create a dictionary to restore all items that are selected
        order_items = {
            'items': []
        }

        #get those items
        items = request.POST.getlist('items[]')

        for item in items:

            menu_item = MenuItem.objects.get(pk__contains= int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,
            }

            #append item selected
            order_items['items'].append(item_data)


            price = 0
            item_ids = []
        for item in order_items['items']:
                price += item['price']
                item_ids.append(item['id'])

        order = OrderModel.objects.create(
            price=price,
            name=name,
            email=email,
            street=street,
            city=city,
            state=state,
            zip_code=zip_code     
        )

        order.items.add(*item_ids)

        #After everything is done, send confirmation mail to the user

        body = ('Thank you for order! Your food is being made and will be delivered soon\n'
        f'Your total: {price}\n'
        'THANK YOU AGAIN!'
        )
        send_mail(
            'Your order',
            body,
            'example@example.com',
            [email],
            fail_silently=False
        )
        # order_id = OrderModel.objects.get(= int(item))


        context = {
                'items': order_items['items'],
                'price': price,
                'order_id': order.id
            }
        return render(request, 'customer/order_confirmation.html', context)

        # return redirect('order-confirmation', pk=order.pk)

#Mbaye
class Order(View):
    def get(self, request, *args, **kwargs):
        
          #Get every item from each category
        appetizers = MenuItem.objects.filter(category__name__contains='appetizer')
        entres = MenuItem.objects.filter(category__name__contains='Entre')
        desserts = MenuItem.objects.filter(category__name__contains='Dessert')
        drinks = MenuItem.objects.filter(category__name__contains='Drink')
          #pass into context
        context = {

              'appetizers': appetizers,
              'entres': entres,
              'desserts': desserts,
              'drinks': drinks
          }
          #render the template 
        return render(request, 'customer/order.html', context)


    def post(self, request, *args, **kwargs):
        """
        grab all the selected items
        get the menu item for that item that's seleected
        return the name,  price and id to figure out some calculations on the price 
        
        and return something lateer
        """
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        #create a dictionary to restore all items that are selected
        order_items = {
            'items': []
        }
        #get those items selected and save in a list
        items = request.POST.getlist('items[]')
        print("items",items)
        for item in items:

            menu_item = MenuItem.objects.get(pk__contains= int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,
            }

            #append item selected
            order_items['items'].append(item_data)
        print("order_items",order_items)


        price = 0
        item_ids = []
        for item in order_items['items']:
                price += item['price']
                item_ids.append(item['id'])
        print("item_ids",item_ids)
        order = OrderModel.objects.create(
            price=price,
            name=name,
            email=email,
            street=street,
            city=city,
            state=state,
            zip_code=zip_code     
        )

        order.items.add(*item_ids)

        #After everything is done, send confirmation mail to the user

        body = ('Thank you for order! Your food is being made and will be delivered soon\n'
        f'Your total: {price}\n'
        'THANK YOU AGAIN!'
        )
        send_mail(
            'Your order',
            body,
            'example@example.com',
            [email],
            fail_silently=False
        )
        # order_id = OrderModel.objects.get(= int(item))


        context = {
                'items': order_items['items'],
                'price': price,
                'order_id': order.id
            }
        # return render(request, 'customer/order_confirmation.html', context)

        return redirect('order-confirmation', pk=order.pk)





class OrderConfirmation(View): 

    def get(self, request,pk , *args, **kwargs):
    # order = OrderModel.objects.filter(pk= pk)  id = kwargs['pk']
        orderSet = OrderModel.objects.all()
        serializer_class = OrderSerializer
        order = OrderModel.objects.filter(pk=pk)
        # if not order:
        #     return Response({
        #         "status": "failure",
        #         "message": "no such item.",
        #     }, status = status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order, many = True)

        order_items = {
            'items': []
        }
        items = serializer.data[0]['items']
        for item in items:
            menu_item = MenuItem.objects.get(pk__contains= int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,
            }

            #append item selected
            order_items['items'].append(item_data)
        print("order_items",order_items)

        context = {
            'status': "success",
            'message': "item successfully retrieved.",
            'count': order.count(),
            'items': order_items['items'],
            'price': serializer.data[0]['price'],

        }

        return render(request, 'customer/order_confirmation.html', context)

    def post(self, request, pk, *args, **kwargs):
        print(request.body)
        
#Mbaye
class OrderConfirmation1(View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        context = {
            'pk': order.pk,
            'items': order.items,
            'price': order.price
        }
        return render(request, 'customer/order_confirmation.html', context)
    
    def post(self, request, pk, *args, **kwargs):
        print(request.body)


class OrderPayConfirmation(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/order_pay_confirmation.html')


class Menu(View):

    def get(self, request, *args, **kwargs):
        menu_items = MenuItem.objects.all()

        context ={
            'menu_items': menu_items
        }

        return render(request, 'customer/menu.html', context)



class MenuSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")


        menu_items = MenuItem.objects.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query) |
            Q(description__icontains=query)
        )

        context = {
            'menu_items': menu_items
        }

        return render(request, 'customer/menu.html', context)