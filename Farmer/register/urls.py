from django.urls import path, include
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login),
    path('logout/', views.logout_user),
    path('logout_page/', views.logout_page),
]