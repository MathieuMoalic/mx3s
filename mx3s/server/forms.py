from django import forms

from .models import Simulation


class ScriptUploadForm(forms.ModelForm):
    class Meta:
        model = Simulation

        fields = ('script', )
