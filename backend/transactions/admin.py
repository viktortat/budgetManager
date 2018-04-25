from django.contrib import admin

from .models import Category, Transaction, Wallet, Budget

admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Wallet)
admin.site.register(Budget)
