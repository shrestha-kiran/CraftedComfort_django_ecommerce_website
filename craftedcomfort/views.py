from django.shortcuts import render

# Create your views here.

from product.models import Product, Category


def frontpage(request):
    products = Product.objects.all()[0:8]

    return render(request, 'craftedcomfort/frontpage.html', {'products': products})
