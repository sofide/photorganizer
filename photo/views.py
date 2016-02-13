from django.shortcuts import render
from photo.models import Folder


def home(request):
    return render(
        request,
        'photo/photohome.html',
        {'carpetas': Folder.objects.filter(tipo='origen').order_by('ruta')}
    )

def path_manager(request):
    return render(request,
        'photo/prueba.html')
