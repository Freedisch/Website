from django.http import HttpResponse, request
from django.shortcuts import render
from .models import Product

# Create your views here.
def homepage(request):
    products=Product.objects.all()

    data={
        'products':products
    }
    return render(request,"DealCom/Home.html",data)

def about(request):
    return render(request,"DealCom/AboutUs.html")
def product(request):
    return render(request,"DealCom/Product.html")