from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='Slug(URL)')

    # Создадим имя таблицы
    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

# Таблица с информацией о товарах

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    slug = models.SlugField(max_length=200, unique=True, null=True, verbose_name='Slug(URL)')
    description = models.TextField(blank=True, null=True, verbose_name='Product description')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Picture')
    # В классе models.DecimalField указываем дробную часть цены, количество цифр до точки и количество цифр после точки.
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Price')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Discount in percent')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantity')
    # Если на категорию будут ссылки с таварами то эту категорию нельзя будет удалить - PROTECT
    # CASCADE - это удаление всего того что было в категории вместе с самой категорией.
    # Если удалить категорию то всё что было в ней тоже удалиться.
    # SET_DEFAULT - Установите значение ForeignKey по умолчанию ForeignKeyдолжно быть установлено значение по умолчанию.
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Category')

    class Meta:
        db_table = 'proguct'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name} quantity - {self.quantity}'

    def display_id(self):
        return f'{self.id:05}'  # Добавляем пять символов

    def sell_price(self):
        if self.discount:
            result_price = round(self.price - self.price / 100 * self.discount, 2)
            return f'{result_price}'
        return self.price