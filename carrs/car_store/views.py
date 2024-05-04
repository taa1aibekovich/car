from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


class CategoryView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'category_list.html'
    context_object_name = 'car'

class ProductDetailView(DetailView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'category_datail.html'
    context_object_name = 'car'
