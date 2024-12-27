from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from . import models, forms, serializers
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics


class OutflowListView(LoginRequiredMixin, ListView):
    model = models.Outflow
    template_name = 'Outflow_list.html'
    context_object_name ='outflows'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
    
class OutflowCreateView(LoginRequiredMixin, CreateView):
    model = models.Outflow
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list')

class OutflowDetailView(LoginRequiredMixin, DeleteView):
    model = models.Outflow
    template_name = 'outflow_detail.html'

class OutflowCreateListApiView(generics.ListCreateAPIView):
    queryset = models.Outflow.objects.all()
    serializer_class = serializers.OutflowSerializer

class OutflowRetrieveUpdateDestroyApiView(generics.RetrieveDestroyAPIView):
    queryset = models.Outflow.objects.all()
    serializer_class = serializers.OutflowSerializer    