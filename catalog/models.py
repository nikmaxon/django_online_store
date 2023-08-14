from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='категория')
    description = models.TextField(**NULLABLE, verbose_name="описание")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    product_name = models.CharField(max_length=250, verbose_name="наименование")
    description = models.TextField(verbose_name="описание"),
    preview_img = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='превью')
    category = models.ForeignKey(Category, **NULLABLE, on_delete=models.CASCADE, verbose_name="категория")
    price = models.IntegerField(verbose_name='цена')
    creation_date = models.DateField(auto_now_add=True, verbose_name='дата создания')
    last_change_date = models.DateField(auto_now=True, verbose_name='дата последнего изменения')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'Название: {self.product_name} (Категория:{self.category}): Цена:{self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

        permissions = [
            (
                'set_published',
                'Can publish posts'
            ),
            (
                'set_category',
                'Can change category'
            ),
            (
                'set_description',
                'Can change description'
            ),
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, **NULLABLE, on_delete=models.CASCADE, verbose_name="продукт")
    version_number = models.CharField(max_length=150, verbose_name='номер версии')
    version_name = models.CharField(max_length=150, verbose_name='название версии')
    version_sing = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product} Версия:{self.version_name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
