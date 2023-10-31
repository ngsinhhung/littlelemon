from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=1000, default="")

    def __str__(self):
        return self.name


