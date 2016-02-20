import glob, shutil, os
from django.shortcuts import render, redirect, get_object_or_404
from photo.models import Folder
from .forms import FormFolder

def home(request):

    if request.method == "POST":
        form = FormFolder(request.POST)

        if form.is_valid():
            folder = form.save(commit=False)

            if Folder.objects.filter(ruta = folder.ruta) == []:

                if folder.ruta[-1] != '/':
                    folder.ruta = folder.ruta + '/'

                folder.tipo = 'origen'

                folder.save()

            #eliminar elif cuando borre rutas duplicadas de la bd
            elif len(Folder.objects.filter(ruta = folder.ruta)) > 1:
                return redirect('photo.views.visor',
                pk = Folder.objets.filter(ruta = folder.ruta)[0].id)

            else:
                folder = Folder.objects.get(ruta = folder.ruta)
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

    def listarFotos(ruta):
        photosList = glob.glob(ruta + '*.jpg')
        for i in glob.glob(ruta + '*.JPG'): photosList.append(i)
        for i in glob.glob(ruta + '*.png'): photosList.append(i)
        for i in glob.glob(ruta + '*.PNG'): photosList.append(i)
        for i in glob.glob(ruta + '*.jpeg'): photosList.append(i)
        for i in glob.glob(ruta + '*.JPEG'): photosList.append(i)
        return photosList

    photosList = listarFotos(carpetaActual.ruta)

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

            photosList = listarFotos(carpetaActual.ruta)

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
