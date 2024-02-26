from django import forms
from . import models

class TattooForm(forms.ModelForm):
    class Meta:
        model = models.Tattoo
        fields = '__all__'

class DesignForm(forms.ModelForm):
    class Meta:
        model = models.Design
        fields = '__all__'
        widgets = {
            "available": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            }