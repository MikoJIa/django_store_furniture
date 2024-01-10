from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404

from goods.models import Products, Categories





def catalog(request, category_slug, page=1):
    if category_slug == 'all-goods':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)  # Мы теперь будет отоброжать страницу которую хотим отоброзить

    context = {
        'title': 'HOME - каталог',
        'goods': current_page,
        'slug_url': category_slug,

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
