from django.db import models


class Persone(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    profession = models.ForeignKey('Profession', on_delete=models.SET_NULL, null=True)


class Profession(models.Model):
    profession_name = models.CharField(max_length=100)
    price = models.FloatField(default=0)