from django  import forms
from .models import Folder

class OrigenFolder(forms.ModelForm):

    class Meta:
        model = Folder
        fields = ('ruta',)
