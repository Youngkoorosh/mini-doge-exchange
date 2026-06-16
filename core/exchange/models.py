from django.db import models

class Wallet(models.Model):
    balance_usdt = models.FloatField(default=1000)
    doge = models.FloatField(default=0)