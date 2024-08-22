from django.contrib import admin
from newapp.models import User
from .models import Product, CartItem

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product)
admin.site.register(CartItem)

