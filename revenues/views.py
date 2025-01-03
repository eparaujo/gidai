from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from . import models, forms, serializers
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from app import metrics
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics


class RevenueListView(LoginRequiredMixin, ListView):
    model = models.Revenue
    template_name = 'revenue_list.html'
    context_object_name ='revenues'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['revenue_metrics'] = metrics.get_revenue_metrics()

        return context
    
class RevenueCreateView(LoginRequiredMixin, CreateView):
    model = models.Revenue
    template_name = 'revenue_create.html'
    form_class = forms.RevenueForm
    success_url = reverse_lazy('revenue_list')
    

class RevenueDetailView(LoginRequiredMixin, DeleteView):
    model = models.Revenue
    template_name = 'revenue_detail.html'

class RevenueUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Revenue
    template_name = 'revenue_update.html'
    form_class = forms.RevenueForm
    success_url = reverse_lazy('revenue_list')

class RevenueDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Revenue
    template_name = 'revenue_delete.html'
    success_url = reverse_lazy('revenue_list')

class RevenueCreateListApiView(generics.ListCreateAPIView):
    queryset = models.Revenue.objects.all()
    serializer_class = serializers.RevenueSerializer

class RevenueRetrieveUpdateDestroyApiView(generics.RetrieveDestroyAPIView):
    queryset = models.Revenue.objects.all()
    serializer_class = serializers.RevenueSerializer       