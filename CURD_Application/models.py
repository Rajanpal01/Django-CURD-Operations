from django.db import models

# Create your models here.
class Show(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    Email = models.EmailField()

    def __str__(self):
        return self.name