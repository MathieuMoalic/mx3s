from django.shortcuts import redirect, get_object_or_404, render
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Simulation
from .forms import ScriptUploadForm,FileFieldForm
from django.contrib.auth.models import User

class IndexView(generic.ListView):
    template_name = 'server/index.html'
    context_object_name = 'context'

    def get_queryset(self):
        return {
            'queued': Simulation.objects.filter(is_queued=True),
            'running': Simulation.objects.filter(is_running=True),
            'finished': Simulation.objects.filter(is_finished=True),
            'users': User.objects.all(),
        }

    def post(self, request):
        form = ScriptUploadForm(request.POST, request.FILES)

        if form.is_valid():
            files = request.FILES.getlist('script')
            for f in files:
                print(f)

            form.save()
            # import pdb
            # pdb.set_trace()
            messages.success(request, 'success', extra_tags='alert')

        else:
            messages.error(request,
                           "This file couldn't be uploaded",
                           extra_tags='alert')
        return redirect(request.META['HTTP_REFERER'])

class DeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Simulation
    success_url = '/'
    success_message = 'deleted...'

    def delete(self, request, *args, **kwargs):
        name = self.get_object().name
        request.session['name'] = name
        message = request.session['name'] + ' deleted successfully'
        messages.success(self.request, message)
        return super(DeleteView, self).delete(request, *args, **kwargs)


def redirect_sim(request, sim_id):
    simulation_instance = get_object_or_404(Simulation, pk=sim_id)
    url = f'http://{simulation_instance.ip}:{simulation_instance.port}/'
    return redirect(url)
