import glob, os

def listarFotos(ruta):
    photosList = glob.glob(ruta + '*.jpg')
    for i in glob.glob(ruta + '*.JPG'): photosList.append(i)
    for i in glob.glob(ruta + '*.png'): photosList.append(i)
    for i in glob.glob(ruta + '*.PNG'): photosList.append(i)
    for i in glob.glob(ruta + '*.jpeg'): photosList.append(i)
    for i in glob.glob(ruta + '*.JPEG'): photosList.append(i)
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
