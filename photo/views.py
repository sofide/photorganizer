import glob, shutil, os
from django.shortcuts import render, redirect, get_object_or_404
from photo.models import Folder
from .forms import FormFolder

def home(request):

    if request.method == "POST":
        form = FormFolder(request.POST)

        if form.is_valid():
            folder = form.save(commit=False)

            if folder.ruta[-1] != '/':
                folder.ruta = folder.ruta + '/'

            folder.tipo = 'origen'

            folder.save()

            return redirect('photo.views.visor', pk=folder.id)


    else:
        form = FormFolder()

    return render(
        request,
        'photo/photohome.html',
        {'carpetas': Folder.objects.filter(tipo='origen').order_by('ruta'),
        'form': form}
    )

def visor(request, pk):
    carpetaActual = get_object_or_404(Folder, pk=pk)

    photosList = glob.glob(carpetaActual.ruta + '*.jpg')

    if request.method == "POST":
        form = FormFolder(request.POST)

        if form.is_valid():
            folder = form.save(commit=False)

            if folder.ruta[-1] != '/':
                folder.ruta = folder.ruta + '/'

            if not os.path.exists(folder.ruta):
                try:
                    os.makedirs(folder.ruta)
                except:
                    return render(
                        request,
                        'photo/visor.html',
                        {'carpetas': Folder.objects.filter(tipo='destino').order_by('ruta'),
                        'form': form,
                        'fotos': photosList,
                        'carpeta': carpetaActual,
                        'error': "No se puede crear la carpeta espcificada"
                        }
                    )

            folder.tipo = 'destino'

            folder.save()

            shutil.move(photosList[0], folder.ruta)

            photosList = glob.glob(carpetaActual.ruta + '*.jpg')

    else:
        form = FormFolder()

    if photosList == []:
        return render(
        request,
        'photo/visor.html',
        {'error': "No hay fotos en esa carpeta!",
        'carpeta': carpetaActual,
        }
        )

    else:
        return render(
            request,
            'photo/visor.html',
            {'carpetas': Folder.objects.filter(tipo='destino').order_by('ruta'),
            'form': form,
            'fotos': photosList,
            'carpeta': carpetaActual,
            }
        )
