from django.shortcuts import render

from apps.product.models import Category, Product


def index(request):
    category_third_block = Category.objects.filter(stat_third_block=True)[:3]
    sliders_product = Product.objects.all().order_by('-id')[:3]
    latest_product = Product.objects.all().order_by('-id')[:6]
    category_menu = Category.objects.all()  
    context = { 
        'sliders_product':sliders_product,
        'category_menu':category_menu,
        'latest_product':latest_product,
        'category_third_block':category_third_block,
    }
    return render(request, 'index.html', context)