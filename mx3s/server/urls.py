from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "server"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:sim_id>/", views.redirect_sim, name="redirect-sim"),
    # path("upload/", views.ScriptUploadView, name="upload"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)