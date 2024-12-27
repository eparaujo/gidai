from django import forms
from . import models


class WithdrawalForm(forms.ModelForm):

    class Meta:
        model = models.Withdrawal
        fields = ['goal', 'value',]
        widgets = {
            'goal': forms.Select(attrs={'class': 'form-control'}),
            'value':  forms.NumberInput(attrs={'step': '0.01', 'placeholder': '0.00'}),
            
        }
        labels = {
            'goal': 'Meta Financeira',
            'value':'Valor',
            
        }