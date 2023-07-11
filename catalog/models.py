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
    creation_date = models.DateField(**NULLABLE, verbose_name='дата создания')
    last_change_date = models.DateField(**NULLABLE, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.product_name} ({self.category}): {self.price}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
