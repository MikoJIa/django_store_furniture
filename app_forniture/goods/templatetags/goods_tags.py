from goods.models import Categories

from django import template


# Нам необходимо зарегистрировать этот шаблонный тег

register = template.Library()
@register.simple_tag()
def teg_categories():
    return Categories.objects.all()