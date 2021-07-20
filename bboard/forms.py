from django.forms import ModelForm
from django import forms
from .models import Bb

class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = '__all__'

        labels = {
            'title': '',
            'rubric': '',
            'description': '',
            'price': '',
            'date': '',
            'city': '',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            'rubric': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Рубрика'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата'}),
            'city': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Город'})
        }
