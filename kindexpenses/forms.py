from django import forms
from . import models


class KindExpenseForm(forms.ModelForm):

    class Meta:
        model = models.KindExpense
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
        }
        labels = {
            'name': 'Tipo de Despesa',
            'description': 'Descrição',
        } 