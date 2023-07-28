from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import cloths, category,cart

admin.site.register(cloths)
admin.site.register(category)
admin.site.register(cart)
