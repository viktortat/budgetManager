import datetime
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

TRANSACTION_TYPES = [
    ('expense', _('Expense')),
    ('income', _('Income')),
]

User = get_user_model()


class Wallet(models.Model):
    name = models.CharField(_("Name"), max_length=128)
    owner = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE, blank=True, null=True)
    users = models.ManyToManyField(User, related_name="users", verbose_name=_('Users'), blank=True)
    balance = models.DecimalField(_('Balance'), max_digits=11, decimal_places=2, default=0.0)

    def update_total(self):
        balance = Decimal(0.0)
        for category in self.categories.all():
            balance += category.balance
        self.balance = format(balance, ".2f")
        self.save()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(_("Name"), max_length=128)
    color = models.CharField(_("Color"), max_length=16)
    wallet = models.ForeignKey(Wallet, verbose_name=_("Wallet"), related_name="categories", on_delete=models.CASCADE, blank=True, null=True)
    balance = models.DecimalField(_('Balance'), max_digits=11, decimal_places=2, default=0.0)

    def update_total(self):
        balance = Decimal(0.0)
        for transaction in self.transactions.all():
            if transaction.transaction_type == 'expense':
                balance -= transaction.amount
            else:
                balance += transaction.amount
        self.balance = format(balance, ".2f")
        self.save()

    def __str__(self):
        return self.name


class Transaction(models.Model):
    transaction_type = models.CharField(_('Transaction type'), max_length=32, choices=TRANSACTION_TYPES, default='expense')
    notes = models.CharField(_('Notes'), max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name=_('Category'), related_name='transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(_('Amount'), max_digits=11, decimal_places=2)
    date = models.DateField(_('Date'), default=datetime.date.today)
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE, blank=True, null=True)


def post_save_balance(sender, instance, created, *args, **kwargs):
    category_id = instance.category.id
    category = Category.objects.get(id=category_id)
    if category is not None:
        category.update_total()
        if category.wallet is not None:
            category.wallet.update_total()


post_save.connect(post_save_balance, sender=Transaction)
