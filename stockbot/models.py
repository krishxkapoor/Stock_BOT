from django.db import models
from django.contrib.auth.models import User

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=20)
    added_at = models.DateTimeField(auto_now_add=True)

class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=20)
    alert_type = models.CharField(max_length=10, choices=[("price", "Price"), ("percent", "Percent")])
    value = models.FloatField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Signal(models.Model):
    symbol = models.CharField(max_length=20)
    buy_prob = models.FloatField()
    hold_prob = models.FloatField()
    sell_prob = models.FloatField()
    computed_at = models.DateTimeField(auto_now_add=True)