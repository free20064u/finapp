from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signIn/', views.signInView, name ='signIn'),
    path('signOut/', views.signOutView, name ='signOut'),
    path('adminRegister/', views.adminRegisterView, name='adminRegister')
]
