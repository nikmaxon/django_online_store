from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class Material(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.SlugField(max_length=100)
    body = models.TextField(**NULLABLE, verbose_name='содержимое')
    preview = models.ImageField(upload_to='materials/', **NULLABLE, verbose_name='превью')
    creation_date = models.DateField(auto_now_add=True, verbose_name='дата создания')
    published = models.BooleanField(default=False, verbose_name='признак публикации')
    views = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'


