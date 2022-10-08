from django.db import models
from django.contrib.postgres.fields import ArrayField


class State(models.Model):
    title = models.CharField(max_length=150)
    matrix = ArrayField(ArrayField(ArrayField(models.IntegerField())))

    def __str__(self):
        return self.title


class Matrices(models.Model):
    matrix = ArrayField(ArrayField(models.IntegerField()))
