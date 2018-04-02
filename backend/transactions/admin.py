from django.contrib import admin

from .models import Category, Transaction, Wallet

admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Wallet)
