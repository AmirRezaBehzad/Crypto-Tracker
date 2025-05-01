from django.db import models
from django.conf import settings

class Deposit(models.Model):
    class Status(models.TextChoices):
        PENDING   = 'pending',   'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        FAILED    = 'failed',    'Failed'

    user     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount   = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10, default='USDT')
    trx_id   = models.CharField(max_length=200, unique=True)
    status   = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    created  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} | {self.amount} {self.currency} | {self.get_status_display()}"

    @classmethod
    def user_deposits(cls, user):
        """Return all deposits for a given user."""
        return cls.objects.filter(user=user)
