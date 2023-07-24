# Generated by Django 4.2.3 on 2023-07-24 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='body',
            field=models.TextField(verbose_name='содержимое'),
        ),
        migrations.AlterField(
            model_name='material',
            name='published',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='признак публикации'),
        ),
        migrations.AlterField(
            model_name='material',
            name='slug',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='title',
            field=models.CharField(max_length=300, verbose_name='заголовок'),
        ),
        migrations.AlterField(
            model_name='material',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='количество просмотров'),
        ),
    ]
