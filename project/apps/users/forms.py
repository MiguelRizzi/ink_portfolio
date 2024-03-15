from django import forms
from .models import Avatar

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['image']
        labels = {'image': 'Imagen'}