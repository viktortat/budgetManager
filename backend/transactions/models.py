import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

TRANSACTION_TYPES = [
    ('expense', _('Expense')),
    ('income', _('Income')),
]

User = get_user_model()


class Category(models.Model):
    name = models.CharField(_("Name"), max_length=128)
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    transaction_type = models.CharField(_('Transaction type'), max_length=32, choices=TRANSACTION_TYPES, default='expense')
    notes = models.CharField(_('Notes'), max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name=_('Category'), related_name='transactions', on_delete=models.PROTECT)
    amount = models.DecimalField(_('Amount'), max_digits=11, decimal_places=2)
    date = models.DateField(_('Date'), default=datetime.date.today)
    user = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE, blank=True, null=True)
