from django.contrib import admin
from .models import Customer
from .models import Product
from .models import ProductReview
from .models import Order
from .models import OrderItem

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(ProductReview)
admin.site.register(Order)
admin.site.register(OrderItem)