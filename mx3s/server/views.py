from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Simulation


class IndexView(generic.ListView):
    template_name = "server/index.html"
    context_object_name = "sim_obj"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Simulation.objects.all()[:5]
