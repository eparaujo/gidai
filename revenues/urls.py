from django.urls import path
from . import views

urlpatterns = [
    path('revenues/list/', views.RevenueListView.as_view(), name='revenue_list'), # a utilização do name aqui, serve por exemplo para ser usada no HTML no método de busca
    path('revenues/create/', views.RevenueCreateView.as_view(), name='revenue_create'),
    path('revenues/<int:pk>/detail/', views.RevenueDetailView.as_view(), name='revenue_detail'),
    path('revenues/<int:pk>/update/', views.RevenueUpdateView.as_view(), name='revenue_update'),
    path('revenues/<int:pk>/delete/', views.RevenueDeleteView.as_view(), name='revenue_delete'),

    path('api/v1/revenues/', views.RevenueCreateListApiView.as_view(), name='revenue-create-list-api-view'),
    path('api/v1/revenues/<int:pk>/', views.RevenueRetrieveUpdateDestroyApiView.as_view(), name='revenue-retrieve-list-api-view'), 
]