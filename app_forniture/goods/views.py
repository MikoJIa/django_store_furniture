from django.shortcuts import render

from goods.models import Products, Categories


def catalog(request):
    goods = Products.objects.all()

    context = {
        'title': 'HOME - каталог',
        'goods': goods

    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug=False, product_id=False):
    if product_id:
        products = Products.objects.get(id=product_id)
    else:
        products = Products.objects.get(slug=product_slug)

    context = {
        'products': products
    }

    return render(request, "goods/product.html", context)
