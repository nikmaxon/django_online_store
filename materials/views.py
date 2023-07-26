from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from pytils.translit import slugify

from materials.models import Material


# Create your views here.
class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'body',)
    success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_material = form.save()
            new_material.slug = slugify(new_material.title)
            new_material.save()
        return super().form_valid(form)


class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy('materials:list')


class MaterialUpdateView(UpdateView):
    model = Material
    fields = ('title', 'body',)
    #success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_material = form.save()
            new_material.slug = slugify(new_material.title)
            new_material.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('materials:view', args=[self.kwargs.get('pk')])


class MaterialListView(ListView):
    model = Material

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)

        return queryset


class MaterialDetailView(DetailView):
    model = Material
    template_name = 'materials/material_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object
