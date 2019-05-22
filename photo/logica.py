import glob, os
from photo.models import ImagenRechazada

def listarFotos(carpeta):
    photosList = [file_name
                  for file_name in glob.glob(carpeta.ruta + '*.*')
                  if file_name.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'gif'))]
    photosList = list(sorted(photosList))
    rechazadas = ImagenRechazada.objects.filter(carpeta=carpeta)
    no_mostrar =[]
    for foto in rechazadas:
        no_mostrar.append(foto.ruta)

    mostrar = []

    for foto in photosList:
        if foto not in no_mostrar:
            mostrar.append(foto)

    return mostrar[0:30]


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
