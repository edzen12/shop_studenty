from django.shortcuts import render

from apps.product.models import Category, Product

# Create your views here.
def index(request):
    sliders_product = Product.objects.all().order_by('-id')[:3]
    category_menu = Category.objects.all() 
    context = {
        'sliders_product':sliders_product,
        'category_menu':category_menu
    }
    return render(request, 'index.html', context)