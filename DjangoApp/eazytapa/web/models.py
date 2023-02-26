from django.db import models

# Create your models here.


class Bar(models.Model):
    name = models.CharField(max_length=256)



class Tapa(models.Model):
    name = models.CharField(max_length=256)
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)

    