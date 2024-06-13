from django.shortcuts import render
from .models import Product
# Create your views here.

#def index(request):
 #   return HttpResponse("<h1 style= 'color:brown' >My first webpage with Django</h1>")

def product_list(request):
    products = Product.objects.all()
    context = {
   'products': products,
    }
    return render(request, 'Joshapp/product_list.html', context )



