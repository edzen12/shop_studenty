from django.shortcuts import render

from apps.product.models import Category, Product

# Create your views here.
def index(request):
    mobile_product = Product.objects.all()
    context = {
        'mobile_product':mobile_product
    }
    return render(request, 'mobile.html', context)