from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView

from materials.models import Material


# Create your views here.
class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'body',)
    success_url = reverse_lazy('materials:list')


class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy('materials:list')


class MaterialUpdateView(UpdateView):
    model = Material
    fields = ('title', 'body',)
    success_url = reverse_lazy('materials:list')


class MaterialListView(ListView):
    model = Material


class MaterialDetailView(DetailView):
    model = Material
    template_name = 'materials/material_detail.html'
