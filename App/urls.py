from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import product_list

from .views import (
    HomepageView, AboutpageView, ContactpageView,
    ProductsListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,
)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', HomepageView.as_view(), name='home'),
    path('about/', AboutpageView.as_view(), name='about'),
    path('contact/', ContactpageView.as_view(), name='contact'),
    path('products/', ProductsListView.as_view(), name='product'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/add/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('accounts/', include('accounts.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('products/', views.product_list, name='product-list'),
    path('product/create/', views.product_create, name='product-create'),
    path('products/<int:product_id>/add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('products/<int:product_id>/add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),

              ]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)