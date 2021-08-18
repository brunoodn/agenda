from django.urls import path
from django.views.generic import RedirectView
import core.views


urlpatterns = [
    path('', RedirectView.as_view(url='agenda')),
    path('evento/<titulo>/', core.views.evento),
    path('agenda', core.views.lista_eventos),
]