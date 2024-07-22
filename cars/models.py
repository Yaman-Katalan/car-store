from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model

class Car(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_bought = models.BooleanField(default=False)
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    buy_time = models.DateTimeField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("car-detail", args=[self.id])

    def __str__(self):
        return f"{self.model} ({self.brand})"
