from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Simulation


class IndexView(generic.ListView):
    template_name = "server/index.html"
    context_object_name = "sims"
    # model = Simulation  # same as  queryset = Simulation.objects.all()
    # def get_queryset(self):
    #     queued = Simulation.objects.all()
    #     running = Simulation.objects.all()
    #     finished = Simulation.objects.all()
    #     return Simulation.objects.all()

    # def get_queue(self):
    #     return Simulation.objects.

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context

    def get_queryset(self):

        return {
            "queued": Simulation.objects.filter(is_queued=True),
            "running": Simulation.objects.filter(is_running=True),
            "finished": Simulation.objects.filter(is_finished=True),
        }


class Finished(generic.ListView):
    template_name = "server/finshed.html"
    context_object_name = "sims"

    def get_queryset(self):
        return Simulation.objects.filter(is_finished=True)


class SimulationCreateView(generic.CreateView):
    model = Simulation
    fields = ["path"]


def redirect_view(request):
    return redirect("http://127.0.0.1:35360/")
