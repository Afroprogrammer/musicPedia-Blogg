from django import forms
from django.forms import Textarea, TextInput
from . import models


class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ('title', 'body', 'slug', 'thumb')
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'body': Textarea(attrs={'class': 'form-control'}),
            'slug': TextInput(attrs={'class': 'form-control'}),
        }

