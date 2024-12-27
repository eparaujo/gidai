from django.urls import path
from . import views

urlpatterns = [
    path('goals/list/', views.GoalListView.as_view(), name='goal_list'), # a utilização do name aqui, serve por exemplo para ser usada no HTML no método de busca
    path('goals/create/', views.GoalCreateView.as_view(), name='goal_create'),
    path('goals/<int:pk>/detail/', views.GoalDetailView.as_view(), name='goal_detail'),
    path('goals/<int:pk>/update/', views.GoalUpdateView.as_view(), name='goal_update'),
    path('goals/<int:pk>/delete/', views.GoalDeleteView.as_view(), name='goal_delete'),

    path('api/v1/goals/', views.GoalCreateListApiView.as_view(), name='goal-create-list-api-view'),
    path('api/v1/goals/<int:pk>/', views.GoalRetrieveUpdateDestroyApiView.as_view(), name='goal-retrieve-list-api-view'),
]