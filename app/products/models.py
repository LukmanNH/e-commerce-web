from django.db import models


class Product(models.Model):
    """Products database"""
    title = models.CharField(max_length=225)
    content = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
