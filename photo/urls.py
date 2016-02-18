from django.conf.urls import include, url
from . import views
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^visor/(?P<pk>[0-9]+)/$', views.visor, name='visor'),
    url(r'^(?P<path>.*)$', serve, {'document_root': '/'}),
]
