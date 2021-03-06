import os
from django.db import models
from django.dispatch import receiver
from django.core.validators import ValidationError
from django.contrib.auth.models import User

def file_upload_validator(filename):
    extension = filename.name.split(".")[-1].lower()
    if extension not in ("mx3", "go"):
        raise ValidationError("Wrong File Extension")


def rename_script(instance, filename):  # pylint: disable=unused-argument
    # can do f"{user}/name.mx3 later !
    name = filename.split('/')[-1]
    path = f'queued/{name}'
    return path

class Simulation(models.Model):
    start_time = models.DateTimeField('Time Started',
                                      default=None,
                                      blank=True,
                                      null=True)
    end_time = models.DateTimeField('time ended',
                                    default=None,
                                    blank=True,
                                    null=True)
    is_queued = models.BooleanField(default=True)
    is_running = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    name = models.CharField(max_length=200, default='simulation name')
    script = models.FileField(upload_to=rename_script,
                              null=True,
                              validators=[file_upload_validator])
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @property
    def name(self):
        return self.script.name.split("/")[-1][:-4]

    def __str__(self):
        return self.name


class Gpu(models.Model):
    name = models.CharField(max_length=200)
    current_simulation = models.OneToOneField(Simulation,
                                              on_delete=models.SET_NULL,
                                              null=True,
                                              default=None,
                                              blank=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
                                              

    def __str__(self):
        return self.name


@receiver(models.signals.post_delete, sender=Simulation)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    # pylint: disable=unused-argument
    """
    Deletes file from filesystem
    when corresponding `Simulation` object is deleted.
    """
    if instance.script:
        if os.path.isfile(instance.script.path):
            os.remove(instance.script.path)
