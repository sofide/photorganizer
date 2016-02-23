import glob, os
from photo.models import ImagenRechazada

def listarFotos(carpeta):
    photosList = [file_name
                  for file_name in glob.glob(carpeta.ruta + '*.*')
                  if file_name.lower().endswith(('jpg', 'jpeg', 'png'))]
    photosList = list(sorted(photosList))
    no_mostrar = ImagenRechazada.objects.filter(carpeta=carpeta)

    for foto in photosList:
        if foto in no_mostrar:
            photosList.remove(foto)

    return photosList[0:30]


def acondicionar_ruta(ruta):
    if ruta[-1] != '/':
        ruta = ruta + '/'
    return ruta

def comprobar_carpeta(ruta):
    if not os.path.exists(ruta):
        try:
            os.makedirs(ruta)
        except:
            return "error"
    pass
