from django import forms
from . import models


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = models.Expense
        fields = ['name',  'expenses', 'description', 'duedate', 'paid', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'expenses': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'duedate': forms.TextInput(attrs={'placeholder': 'DD-MM','class': 'form-control' }),
            'paid': forms.Select(choices=[(True, 'Sim'), (False, 'Não')]),
            #'value':  forms.NumberInput(attrs={'step': '0.01', 'placeholder': '0.00'}),
        }
        labels = {
            'name': 'Nome',
            'expenses': 'Categoria da Despesa',
            'description': 'Descrição',
            'duedate': 'Data de Vencimento',
            'paid': 'Pago - Não Pago?',           
            #'value': 'Valor Final com Multa e Juros',
        }