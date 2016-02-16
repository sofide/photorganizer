from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^visor/(?P<pk>[0-9]+)/$', views.visor, name='visor'),
]
