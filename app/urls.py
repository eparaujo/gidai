from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api/v1/', include('authentication.urls')),    
    #path('accounts/', include('django.contrib.auth.urls')),

    path('', include('categories.urls')),
    path('', include('expenses.urls')),
    path('', include('revenues.urls')),
    path('', include('kindexpenses.urls')),
    path('', include('inflows.urls')),
    path('', include('outflows.urls')),
    path('', include('goals.urls')),
    path('', include('deposits.urls')),
    path('', include('withdrawals.urls')),

]
