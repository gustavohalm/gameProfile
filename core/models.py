from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit_store = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    credit_card = models.CharField(max_length=55, null=True, blank=True)
    document = models.CharField(max_length=24, null=True, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
