from django.urls import path
from . import views

urlpatterns = [
    path('withdrawals/list/', views.WithdrawalListView.as_view(), name='withdrawal_list'), # a utilização do name aqui, serve por exemplo para ser usada no HTML no método de busca
    path('withdrawals/create/', views.WithdrawalCreateView.as_view(), name='withdrawal_create'),
    path('withdrawals/<int:pk>/detail/', views.WithdrawalDetailView.as_view(), name='withdrawal_detail'),

    path('api/v1/withdrawals/', views.WithdrawalCreateListApiView.as_view(), name='withdrawal-create-list-api-view'),
    path('api/v1/withdrawals/<int:pk>/', views.WithdrawalRetrieveUpdateDestroyApiView.as_view(), name='withdrawal-retrieve-list-api-view'), 
]