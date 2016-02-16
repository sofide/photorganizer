import glob
from django.shortcuts import render, redirect, get_object_or_404
from photo.models import Folder
from .forms import OrigenFolder

def home(request):

    if request.method == "POST":
        form = OrigenFolder(request.POST)

        if form.is_valid():
            folder = form.save(commit=False)

            if folder.ruta[-1] != '/':
                folder.ruta = folder.ruta + '/'

            folder.tipo = 'origen'

            folder.save()

            return redirect('photo.views.visor', pk=folder.id)


    else:
        form = OrigenFolder()

    return render(
        request,
        'photo/photohome.html',
        {'carpetas': Folder.objects.filter(tipo='origen').order_by('ruta'),
        'form': form}
    )

def visor(request, pk):
    carpeta = get_object_or_404(Folder, pk=pk)

    photosList = glob.glob(carpeta.ruta + '*.jpg')

    if photosList == []:
        return render(
        request,
        'photo/photohome.html',
        {'error': "No hay fotos en esa carpeta!"}
        )
    else:
        return render(
        request,
        'photo/visor.html',
        {'fotos': photosList, 'carpeta': carpeta}
        )
