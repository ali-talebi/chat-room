from django import forms
from .models import  TextToText
class TextToTextForm(forms.ModelForm):
    class Meta:
        model = TextToText
        fields = ['text' , ]
