import datetime

from django.db import models
from django.utils import timezone


class Server(models.Model):
    ip = models.GenericIPAddressField(default="127.0.0.1")


class Simulation(models.Model):
    start_time = models.DateTimeField(
        "Time Started", default=None, blank=True, null=True
    )
    end_time = models.DateTimeField("time ended", default=None, blank=True, null=True)
    is_queued = models.BooleanField(default=True)
    is_running = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    ip = models.GenericIPAddressField(default="127.0.0.1")
    port = models.PositiveIntegerField(blank=True, null=True, default=None)
    path = models.FilePathField(path="/mnt/g/Mathieu/simulations/server")
    name = models.CharField(max_length=200, default="simulation name")
    script = models.FileField("/", null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)

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