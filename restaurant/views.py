from django.shortcuts import render

# Create your views here.
from django.views import View


class Dashboard(View):
    def get(self, request, *args, **kwargs):
        return render(request,'restaurant/dashboard.html')