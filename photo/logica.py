import glob, os

def listarFotos(ruta):
    photosList = [file_name
                  for file_name in glob.glob(ruta + '*.*')
                  if file_name.lower().endswith(('jpg', 'jpeg', 'png'))]
    photosList = list(sorted(photosList))[0:30]
    return photosList

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
