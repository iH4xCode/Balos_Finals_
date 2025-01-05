from django.contrib import admin
from django.urls import path
from .views import (
    HomepageView, AboutpageView, ContactpageView, LoginformpageView,
    ProductsListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', HomepageView.as_view(), name='home'),
    path('about/', AboutpageView.as_view(), name='about'),
    path('contact/', ContactpageView.as_view(), name='contact'),
    path('loginform/', LoginformpageView.as_view(), name='loginform'),
    path('products/', ProductsListView.as_view(), name='product'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/add/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]