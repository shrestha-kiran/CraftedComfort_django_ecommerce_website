from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from product.models import Product, Category


def frontpage(request):
    products = Product.objects.all()[0:8]

    return render(request, 'craftedcomfort/frontpage.html', {'products': products})

def signup(request):
    return render(request, 'craftedcomfort/signup.html')

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    active_category = request.GET.get('category', '')

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category,
    }

    return render(request, 'craftedcomfort/shop.html', context)
