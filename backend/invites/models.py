import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _
from dry_rest_permissions.generics import authenticated_users, allow_staff_or_superuser

from transactions.models import Wallet

User = get_user_model()

STATUS_OPTIONS = [
    ('pending', _('Pending')),
    ('accepted', _('Accepted')),
    ('refused', _('Refused')),
    ('canceled', _('Canceled')),
]


class Invitation(models.Model):
    date = models.DateField(_('Date'), default=datetime.date.today)
    creator = models.ForeignKey(User, verbose_name=_('Creator'), related_name='creator', on_delete=models.CASCADE)
    invited = models.ForeignKey(User, verbose_name=_('Invited user'), related_name='invited', on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, verbose_name=_("Wallet"), related_name="Invitations", on_delete=models.CASCADE)
    status = models.CharField(_('Status'), max_length=32, choices=STATUS_OPTIONS)

    def __str__(self):
        return self.creator.email + " – " + self.invited.email + " – " + self.wallet.name

    @staticmethod
    @authenticated_users
    @allow_staff_or_superuser
    def has_read_permission(request):
        return True

    @staticmethod
    @authenticated_users
    @allow_staff_or_superuser
    def has_write_permission(request):
        return True

    @authenticated_users
    @allow_staff_or_superuser
    def has_object_read_permission(self, request):
        return request.user == self.creator or request.user == self.invited

    @authenticated_users
    @allow_staff_or_superuser
    def has_object_write_permission(self, request):
        return request.user == self.creator or request.user == self.invited
