from django.urls import path
from . import views

urlpatterns = [
    path('inflows/list/', views.InflowListView.as_view(), name='inflow_list'), # a utilização do name aqui, serve por exemplo para ser usada no HTML no método de busca
    path('inflows/create/', views.InflowCreateView.as_view(), name='inflow_create'),
    path('inflows/<int:pk>/detail/', views.InflowDetailView.as_view(), name='inflow_detail'),
    
    path('api/v1/inflows/', views.InflowCreateListApiView.as_view(), name='inflow-create-list-api-view'),
    path('api/v1/inflows/<int:pk>/', views.InflowRetrieveUpdateDestroyApiView.as_view(), name='inflow-retrieve-list-api-view'),
]