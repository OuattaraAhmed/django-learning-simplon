from django.db import models

# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Simploniens(TimeStamp):
    nom = models.CharField(max_length=10)
    prenom = models.CharField(max_length=15)