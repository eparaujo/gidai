from django.urls import path
from . import views

urlpatterns = [
    path('kindexpense/list/', views.KindExpenseListView.as_view(), name='kindexpense_list'), # a utilização do name aqui, serve por exemplo para ser usada no HTML no método de busca
    path('kindexpense/create/', views.KindExpenseCreateView.as_view(), name='kindexpense_create'),
    path('kindexpense/<int:pk>/detail/', views.KindExpenseDetailView.as_view(), name='kindexpense_detail'),
    path('kindexpense/<int:pk>/update/', views.KindExpenseUpdateView.as_view(), name='kindexpense_update'),
    path('kindexpense/<int:pk>/delete/', views.KindExpenseDeleteView.as_view(), name='kindexpense_delete'),

    
    path('api/v1/kindexpenses/', views.KindexpenseCreateListApiView.as_view(), name='kindexpense-create-list-api-view'),
    path('api/v1/kindexpenses/<int:pk>/', views.KindexpenseRetrieveUpdateDestroyApiView.as_view(), name='kindexpense-retrieve-list-api-view'),
]