from django.db import models

class Room_Type(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=48)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)