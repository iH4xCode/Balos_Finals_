from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product

# Static pages
class HomepageView(TemplateView):
    template_name = 'home.html'

class AboutpageView(TemplateView):
    template_name = 'about.html'

class ContactpageView(TemplateView):
    template_name = 'contact.html'

# Product pages
class ProductpageView(TemplateView):
    template_name = 'product.html'

class LoginformpageView(TemplateView):
    template_name = 'loginform.html'

# Product views
class ProductsListView(ListView):
    model = Product
    template_name = 'Product.html'
    context_object_name = 'product_list'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'description', 'price', 'stock']
    success_url = reverse_lazy('product')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'description', 'price', 'stock']
    success_url = reverse_lazy('product')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product')

