from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('client_dashboard/', views.clientDashboardView, name='client_dashboard'),
    path('admin_dashboard/', views.adminDashboardView, name='admin_dashboard'),
    path('clients/', views.clientsView, name='clients'),
    path('accountType/', views.accountTypeView, name="accountType"),
    path('createAccountType/', views.createAccountTypeView, name="createAccountType"),
    path('deposite/<int:id>/', views.depositeView, name='deposite'),
    path('withdrawal/<int:id>/', views.withdrawalView, name='withdrawal'),
    path('client_profile/', views.clientProfileView, name='client_profile'),
    path('statement/<int:id>/', views.statementView, name='statement'),
    path('transfer/', views.transferView, name='transfer'),
]
