import glob
from django.shortcuts import render, redirect
from photo.models import Folder
from .forms import OrigenFolder

def visor(request, ruta):
    photosList = glob.glob(ruta + '*.jpg')

    if photosList == []:
        return render(
        request,
        'photo/photohome.html',
        {'error': "No hay fotos en esa carpeta!"}
        )
    else:
        return(
        request,
        'visor.html',
        {'fotos': photosList}
        )


def home(request):

    if request.method == "POST":
        form = OrigenFolder(request.POST)

        if form.is_valid():
            folder = form.save(commit=False)

            if folder.ruta[-1] != '/':
                folder.ruta = folder.ruta + '/'

            folder.tipo = 'origen'

            folder.save()

            return redirect('photos.views.visor', ruta=folder.ruta)


    else:
        form = OrigenFolder()

    return render(
        request,
        'photo/photohome.html',
        {'carpetas': Folder.objects.filter(tipo='origen').order_by('ruta'),
        'form': form}
    )
