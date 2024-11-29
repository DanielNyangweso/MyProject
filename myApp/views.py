from django.shortcuts import render
from .models import *
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

def home(request):
    context={}
    return render(request, "myApp/home.html", context)

def products(request):
    products = Product.objects.all()
    context={'products':products}
    return render(request, "myApp/products.html", context)

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer