from django.urls import path
from . import views

urlpatterns = [
    path('deposits/list/', views.DepositListView.as_view(), name='deposit_list'), # a utilização do name aqui, serve por exemplo para ser usada no HTML no método de busca
    path('deposits/create/', views.DepositCreateView.as_view(), name='deposit_create'),
    path('deposits/<int:pk>/detail/', views.DepositDetailView.as_view(), name='deposit_detail'),

    path('api/v1/deposits/', views.DepositCreateListApiView.as_view(), name='deposit-create-list-api-view'),
    path('api/v1/deposits/<int:pk>/', views.DepositRetrieveUpdateDestroyApiView.as_view(), name='deposit-retrieve-list-api-view'),
]