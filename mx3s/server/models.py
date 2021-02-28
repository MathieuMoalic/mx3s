import datetime

from django.db import models
from django.utils import timezone


class Server(models.Model):
    ip = models.GenericIPAddressField(default="127.0.0.1")


class Simulation(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.DateTimeField(
        "time started", default=None, blank=True, null=True
    )
    end_time = models.DateTimeField("time ended", default=None, blank=True, null=True)
    duration = models.DurationField(blank=True, default=None, null=True)
    queued = models.BooleanField()
    running = models.BooleanField()
    finished = models.BooleanField(default=False)
    port = models.PositiveIntegerField(blank=True, null=True, default=None)
    path = models.FilePathField(path="/mnt/g/Mathieu/simulations/server")

    def __str__(self):
        return self.name


class Gpu(models.Model):
    name = models.CharField(max_length=200)
    ip = models.GenericIPAddressField(default="127.0.0.1")
    current_simulation = models.OneToOneField(
        Simulation, on_delete=models.SET_NULL, null=True, default=None, blank=True
    )

    def __str__(self):
        return self.name