from django import forms
from .models import Wiki
from django_summernote.widgets import SummernoteWidget

class WikiForm(forms.ModelForm):
    class Meta:
        model = Wiki
        fields = ['contents']
        widgets = {
            'contents': SummernoteWidget(),
        }
