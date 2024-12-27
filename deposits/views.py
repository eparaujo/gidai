from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import render
from . import models, forms, serializers
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from app import metrics
from goals.models import Goal
from rest_framework import generics


class DepositListView(LoginRequiredMixin, ListView):
    model = models.Deposit
    template_name = 'deposit_list.html'
    context_object_name ='deposits'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        goal = self.request.GET.get('goal')
        
        if goal:
            queryset = queryset.filter(goal__name__icontains=goal)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goal_metrics'] = metrics.get_goal_metrics()
        
        return context
    
    
class DepositCreateView(LoginRequiredMixin, CreateView):
    model = models.Deposit
    template_name = 'deposit_create.html'
    form_class = forms.DepositForm
    success_url = reverse_lazy('deposit_list')

class DepositDetailView(LoginRequiredMixin, DeleteView):
    model = models.Deposit
    template_name = 'deposit_detail.html'

class DepositCreateListApiView(generics.ListCreateAPIView):
    queryset = models.Deposit.objects.all()
    serializer_class = serializers.DepositSerializer

class DepositRetrieveUpdateDestroyApiView(generics.RetrieveDestroyAPIView):
    queryset = models.Deposit.objects.all()
    serializer_class = serializers.DepositSerializer    