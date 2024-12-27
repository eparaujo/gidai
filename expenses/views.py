from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import render
from . import models, forms, serializers
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from app import metrics
from rest_framework import generics


class ExpenseListView(LoginRequiredMixin, ListView):
    model = models.Expense
    template_name = 'expense_list.html'
    context_object_name ='expenses'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expense_metrics'] = metrics.get_expense_metrics()

        return context 

    
class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = models.Expense
    template_name = 'expense_create.html'
    form_class = forms.ExpenseForm
    success_url = reverse_lazy('expense_list')

class ExpenseDetailView(LoginRequiredMixin, DeleteView):
    model = models.Expense
    template_name = 'expense_detail.html'

class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Expense
    template_name = 'expense_update.html'
    form_class = forms.ExpenseForm
    success_url = reverse_lazy('expense_list')

class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Expense
    template_name = 'expense_delete.html'
    success_url = reverse_lazy('expense_list')

class ExpenseCreateListApiView(generics.ListCreateAPIView):
    queryset = models.Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer

class ExpenseRetrieveUpdateDestroyApiView(generics.RetrieveDestroyAPIView):
    queryset = models.Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer     