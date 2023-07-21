from django.db import models

# Create your models here.

class OTP(models.Model):
    email = models.EmailField(unique=True)
    token = models.CharField(max_length=6)
    created_at = models.DateField(auto_now_add=True)