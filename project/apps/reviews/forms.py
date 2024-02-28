from django import forms
from . import models

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['name', 'email', 'rating', 'review']
    
        labels= {
            'name': 'Nombre',
            'email': 'Email',
            'rating': 'Valoración',
            'review': 'Comentario'
        }
        