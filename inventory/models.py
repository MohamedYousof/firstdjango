from django.db import models


class Item(models.Model):
    """for testing """
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
