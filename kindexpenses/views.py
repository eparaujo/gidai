from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from . import models, forms, serializers
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics


class KindExpenseListView(LoginRequiredMixin, ListView):
    model = models.KindExpense
    template_name = 'kindexpense_list.html' 
    context_object_name ='kindexpenses'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
    
class KindExpenseCreateView(LoginRequiredMixin, CreateView):
    model = models.KindExpense
    template_name = 'kindexpense_create.html'
    form_class = forms.KindExpenseForm
    success_url = reverse_lazy('kindexpense_list')

class KindExpenseDetailView(LoginRequiredMixin, DeleteView):
    model = models.KindExpense
    template_name = 'kindexpense_detail.html'

class KindExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = models.KindExpense
    template_name = 'kindexpense_update.html'
    form_class = forms.KindExpenseForm
    success_url = reverse_lazy('kindexpense_list')

class KindExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = models.KindExpense
    template_name = 'kindexpense_delete.html'
    success_url = reverse_lazy('kindexpense_list')

class KindexpenseCreateListApiView(generics.ListCreateAPIView):
    queryset = models.KindExpense.objects.all()
    serializer_class = serializers.KindexpenseSerializer

class KindexpenseRetrieveUpdateDestroyApiView(generics.RetrieveDestroyAPIView):
    queryset = models.KindExpense.objects.all()
    serializer_class = serializers.KindexpenseSerializer