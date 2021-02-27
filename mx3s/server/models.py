import datetime

from django.db import models
from django.utils import timezone


class Simulation(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.DateTimeField("date started")

    def __str__(self):
        return self.name
