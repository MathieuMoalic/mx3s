from django.contrib import admin

from .models import Server, Simulation, Gpu


class SimulationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "start_time",
        "end_time",
        "duration",
        "queued",
        "running",
        "finished",
        "port",
        "path",
        "current_gpu",
    )


class GpuAdmin(admin.ModelAdmin):
    list_display = ("name", "ip", "current_simulation")


admin.site.register(Simulation, SimulationAdmin)
admin.site.register(Gpu, GpuAdmin)
