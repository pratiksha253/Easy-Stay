from django import forms

from .models import BuildingImage


class BuildingImageForm(forms.ModelForm):
    class Meta:
        model = BuildingImage
        fields = '__all__'
        exclude = ['building']
        widgets = {
            "title": forms.TextInput(attrs={"class": ""}),
            
        }
