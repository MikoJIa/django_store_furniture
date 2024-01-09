from django.shortcuts import render, get_object_or_404

from goods.models import Products, Categories




def catalog(request, category_slug):
    if category_slug == 'all-goods':
        goods = Products.objects.all()
    else:
        goods = get_object_or_404(Products.objects.filter(category__slug=category_slug))

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
