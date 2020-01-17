from django.db import models

class Room_Type(models.Model):
    title = models.CharField(max_length=48)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)