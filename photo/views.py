from django.shortcuts import render
from photo.models import Folder
from .forms import OrigenFolder


def home(request):

    if request.method == "POST":
        form = OrigenFolder(request.POST)

        if form.is_valid():
            folder = form.save(commit=False)
            folder.tipo = 'origen'
            folder.save()
    else:
        form = OrigenFolder()

    return render(
        request,
        'photo/photohome.html',
        {'carpetas': Folder.objects.filter(tipo='origen').order_by('ruta')},
        {'form': form},
    )

def path_manager(request):
    return render(request,
        'photo/prueba.html')
