from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models, forms, serializers
from app import metrics
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from rest_framework import generics


class GoalListView(LoginRequiredMixin, ListView):
    model = models.Goal
    template_name = 'goal_list.html'
    context_object_name ='goals'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goal_metrics'] = metrics.get_goal_metrics()
        
        return context
    
class GoalCreateView(LoginRequiredMixin, CreateView):
    model = models.Goal
    template_name = 'Goal_create.html'
    form_class = forms.GoalForm
    success_url = reverse_lazy('goal_list')

class GoalDetailView(LoginRequiredMixin, DeleteView):
    model = models.Goal
    template_name = 'goal_detail.html'

class GoalUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Goal
    template_name = 'goal_update.html'
    form_class = forms.GoalForm
    success_url = reverse_lazy('goal_list')

class GoalDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Goal
    template_name = 'goal_delete.html'
    success_url = reverse_lazy('goal_list')


class GoalCreateListApiView(generics.ListCreateAPIView):
    queryset = models.Goal.objects.all()
    serializer_class = serializers.GoalSerializer

class GoalRetrieveUpdateDestroyApiView(generics.RetrieveDestroyAPIView):
    queryset = models.Goal.objects.all()
    serializer_class = serializers.GoalSerializer        