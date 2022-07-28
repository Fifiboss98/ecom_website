from django.shortcuts import render, get_object_or_404
from store.models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', context={"products": products})

def prod_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'detail.html', context={"product":product})

