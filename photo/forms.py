from django  import forms
from .models import Folder

class FormFolder(forms.ModelForm):

    class Meta:
        model = Folder
        fields = ('ruta',)
