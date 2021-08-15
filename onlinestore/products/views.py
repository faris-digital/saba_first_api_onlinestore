from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from .models import Manufacturer


class ManufacturerListView(ListView):
    model = Manufacturer


class ManufacturerDetailView(DetailView):
    model = Manufacturer
