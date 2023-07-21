from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_card

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/card/', product_card, name='product_card'),

]