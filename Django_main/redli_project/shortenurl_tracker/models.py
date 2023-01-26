from email.policy import default
from django.db import models

# Create your models here.
class data(models.Model):
    entered_url = models.CharField(max_length=50, default="")
    end_url = models.CharField(max_length=50, default="")
    safe = models.CharField(max_length=50, default="")
    domain = models.CharField(max_length=50, default="")
    ip_address = models.CharField(max_length=50, default="")
    spamming = models.CharField(max_length=50, default="")
    Malware = models.CharField(max_length=50, default="")
    Phishing = models.CharField(max_length=50, default="")
    Server = models.CharField(max_length=50, default="")

class s_data(models.Model):
    long_original = models.CharField(max_length=30, default="")
    shorted_url = models.CharField(max_length=30, default="")
