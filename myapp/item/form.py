from django import forms
from .models import SkinType

class SkinTypeForm(forms.ModelForm):

    class Meta:
        model = SkinType
        fields = ('dry','sensitive','oily',)