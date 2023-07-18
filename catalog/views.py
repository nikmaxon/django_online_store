from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def home(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)


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
