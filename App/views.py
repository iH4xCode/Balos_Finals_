from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product, Cart
from datetime import datetime
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.forms import SignupForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .forms import ProductForm
from .models import Product
from .models import Cart
from django.db.models import Q

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')


        send_mail(
            subject=f"New Contact Message from {name}",
            message=message,
            from_email=email,
            recipient_list=['petshopx@protonmail.com'],
        )

        return HttpResponse("Thank you for reaching out! We'll get back to you soon.")

    return render(request, 'contact.html')



def about(request):
    return render(request, 'about.html', {'current_year': datetime.now().year})










@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)


    if request.user.is_authenticated:
        cart_item, created = Cart.objects.get_or_create(
            product=product,
            user=request.user,
            defaults={'quantity': 1}
        )


        if not created:
            cart_item.quantity += 1
            cart_item.save()

    return redirect('cart_view')


def product_list(request):
    query = request.GET.get('q')
    if query:

        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:

        products = Product.objects.all()

    return render(request, 'Product.html', {'product_list': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ProductForm()

    return render(request, 'product_create.html', {'form': form})


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

def cart_view(request):
    user_cart = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart': user_cart})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'



    class LoginForm(forms.Form):
        username = forms.CharField(max_length=100)
        password = forms.CharField(widget=forms.PasswordInput)