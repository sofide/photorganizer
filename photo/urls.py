from django.conf.urls import include, url
from . import views
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^visor/(?P<pk>[0-9]+)/$', views.visor, name='visor'),
    url(r'^eliminar/(?P<pk>[0-9]+)/(?P<volver>[\w])/(?P<carpeta_actual>[0-9]+)?/?$', views.eliminar, name='eliminar'),
    url(r'^mover/(?P<origen>[0-9]+)/(?P<destino>[0-9]+)/$', views.mover, name='mover'),
    url(r'^rechazar/(?P<carpeta>[0-9]+)/$', views.rechazar, name='rechazar'),
    url(r'^ocultas/(?P<carpeta>[0-9]+)/$', views.ocultas, name='ocultas'),
    url(r'^li/(?P<path>.*)$', serve, {'document_root': '/'}),
]
