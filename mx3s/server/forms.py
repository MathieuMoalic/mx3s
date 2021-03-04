from django import forms
# from django.forms.widgets import FileInput

from .models import Simulation


class ScriptUploadForm(forms.ModelForm):
    class Meta:
        model = Simulation
        # widgets = {
        #     'document':
        #     FileInput(attrs={'accept': 'application/pdf,application/msword'})
        # }
        fields = ('script', )
