from django import forms
from . import models


class GoalForm(forms.ModelForm):

    class Meta:
        model = models.Goal
        fields = ['name', 'description', 'goalvalue', 'enddate']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'goalvalue': forms.NumberInput(attrs={'step': '0.01', 'placeholder': '0.00'}),
            #'deposit': forms.NumberInput(attrs={'step': '0.01', 'placeholder': '0.00'}),
            #'withdrawal': forms.NumberInput(attrs={'step': '0.01', 'placeholder': '0.00'}),
            'enddate': forms.TextInput(attrs={'placeholder': 'DD/MM/AAAA','class': 'form-control' }),
        }
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
            'goalvalue': 'Objetivo Financeiro',
            #'deposit': 'Valor Poupado',
            #'withdrawal': 'Valor Debitado',
            'enddate': 'Data para Atingir Objetivo'
        } 