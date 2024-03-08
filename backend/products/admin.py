from django.contrib import admin

# Register your models here.
from .models import Product

admin.site.register(Product)

# user credentials
# cfe, password
# staff, staffpassword