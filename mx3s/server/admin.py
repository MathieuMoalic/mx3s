from django.contrib import admin

from .models import Server, Simulation, Gpu


class SimulationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'start_time',
        'end_time',
        'is_queued',
        'is_running',
        'is_finished',
        'port',
        'path',
        'gpu',
    )


class GpuAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip', 'current_simulation')


admin.site.register(Simulation, SimulationAdmin)
admin.site.register(Gpu, GpuAdmin)
