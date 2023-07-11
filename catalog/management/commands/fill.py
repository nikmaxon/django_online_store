from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        category_list = [
            {'name': 'Мясо', 'description': ''},
            {'name': 'Овощи', 'description': ''},
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )
        Category.objects.bulk_create(category_for_create)

        product_list = [
            {'product_name': 'Курица', 'price': '350'},
            {'product_name': 'Огурец', 'price': '350'},
        ]
        products_for_create = []
        for products_item in product_list:
            products_for_create.append(
                Product(**products_item)
            )
        Product.objects.bulk_create(products_for_create)
