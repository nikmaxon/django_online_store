from django.urls import path
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', cache_page(60)(ProductListView.as_view()), name='home'),
    path('categories/', cache_page(60)(CategoryListView.as_view()), name='categories'),
    path('contacts/', cache_page(60)(contacts), name='contacts'),
    path('cards/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_card'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]
