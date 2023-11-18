from django.db import models

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48, blank=True, null=True)
    email = models.CharField(max_length=120)
    country_code = models.PositiveIntegerField(blank=True, null=True)
    phone = models.PositiveIntegerField(blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)