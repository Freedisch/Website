from django.http import HttpResponse, request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"DealCom/Home.html")

def about(request):
    return render(request,"DealCom/AboutUs.html")
def product(request):
    return render(request,"DealCom/Product.html")