from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'file']
        labels = {
            'title': 'Titulo',
            'body': 'Contenido',
            'file': 'Archivo',
        }
