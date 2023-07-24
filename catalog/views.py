from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


# CBV
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/card.html'


# def product_card(request, pk):
#     product_item = Product.objects.get(pk=pk)
#
#     context = {
#         'object_list': Product.objects.filter(pk=pk),
#         'title': f'Товар :{product_item.product_name}'
#     }
#     return render(request, 'catalog/card.html', context)

def contacts(request):
    if request.method == 'POST' or request.method == 'GET':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name} ({phone}): {message}")

    context = {
        'title': 'Контакты',
    }
    return render(request, 'catalog/contacts.html', context)
