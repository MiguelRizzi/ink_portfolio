from django import forms
from . import models

class TattooForm(forms.ModelForm):
    class Meta:
        model = models.Tattoo
        fields = '__all__'
        labels = {
            "title": "Título",
            "description": "Descripción",
            "image": "Imagen",
        }

class DesignForm(forms.ModelForm):
    class Meta:
        model = models.Design
        fields = '__all__'
        widgets = {
            "available": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            
        }
        labels = {
            "title": "Título",
            "description": "Descripción",
            "image": "Imagen",
            "available": "Disponible",
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
            'phone': forms.NumberInput(attrs={'placeholder': 'Teléfono'}),
            'message': forms.Textarea(attrs={'placeholder': 'Mensaje'})
        }
        labels = {
            'name': 'Nombre',
            'email': 'Correo electrónico',
            'phone': 'Teléfono',
            'message': 'Mensaje'
        }
