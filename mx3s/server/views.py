from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Simulation


class IndexView(generic.ListView):
    template_name = "server/index.html"
    context_object_name = "sim_obj"

    def get_queryset(self):
        return Simulation.objects.all()


class SimulationCreateView(generic.CreateView):
    model = Simulation
    fields = ["path"]


def redirect_view(request):
    return redirect("http://127.0.0.1:35360/")
