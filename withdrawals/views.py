from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from . import models, forms, serializers
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from app import metrics
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics


class WithdrawalListView(LoginRequiredMixin, ListView):
    model = models.Withdrawal
    template_name = 'withdrawal_list.html'
    context_object_name ='withdrawals'
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
    
    
class WithdrawalCreateView(LoginRequiredMixin, CreateView):
    model = models.Withdrawal
    template_name = 'withdrawal_create.html'
    form_class = forms.WithdrawalForm
    success_url = reverse_lazy('withdrawal_list')

class WithdrawalDetailView(LoginRequiredMixin, DeleteView):
    model = models.Withdrawal
    template_name = 'withdrawal_detail.html'

class WithdrawalCreateListApiView(generics.ListCreateAPIView):
    queryset = models.Withdrawal.objects.all()
    serializer_class = serializers.WithdrawalSerializer

class WithdrawalRetrieveUpdateDestroyApiView(generics.RetrieveDestroyAPIView):
    queryset = models.Withdrawal.objects.all()
    serializer_class = serializers.WithdrawalSerializer      