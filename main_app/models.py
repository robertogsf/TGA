from django.db import models
from django.contrib.auth.models import User

class EmergencyContact(models.Model):
    user = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    relationship = models.CharField(max_length=50)

class AlertConfiguration(models.Model):
    user = models.ForeignKey(User, related_name='alerts', on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=50)
    threshold = models.FloatField()
