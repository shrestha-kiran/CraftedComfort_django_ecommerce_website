"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from craftedcomfort.views import frontpage, shop
from product.views import product
from cart.views import add_to_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>', product, name='product'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart')

]
