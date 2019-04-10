from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.CharField(max_length=100, blank=True, default='')
    price = models.IntegerField(default=0)
    summary = models.CharField(max_length=1000, blank=True, default='')
    image = models.CharField(max_length=300, blank=True, default='')
    publisher = models.CharField(max_length=100, blank=True, default='')
