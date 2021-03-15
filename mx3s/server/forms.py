from django import forms

from .models import Simulation


class ScriptUploadForm(forms.ModelForm):
    class Meta:
        model = Simulation
        fields = ('script', )

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))