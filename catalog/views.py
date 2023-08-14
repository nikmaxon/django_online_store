from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)

        return context_data


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.delete_product'
    model = Product
    success_url = reverse_lazy('catalog:home')


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'catalog.view_product'
    model = Product
    template_name = 'catalog/home.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        version_list = Version.objects.all()
        context_data['formset'] = version_list
        return context_data


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/card.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if settings.CACHE_ENABLED:
            key = f'version_list_{self.object.pk}'
            version_list = cache.get(key)
            if version_list is None:
                version_list = self.object.version_set.all()
                cache.set(key, version_list)
        else:
            version_list = self.object.version_set.all()

        context_data['versions'] = version_list
        return context_data


@login_required()
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
