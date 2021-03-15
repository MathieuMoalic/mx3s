from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'server'
urlpatterns = [
    # path('', login_required(views.IndexView.as_view()), name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # path('', views.home, name='index'),
    path('<int:sim_id>/', views.redirect_sim, name='redirect-sim'),
    path('delete/<int:pk>', views.DeleteView.as_view(), name='delete-sim'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
