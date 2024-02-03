from django.urls import path
from authapp import views

urlpatterns = [
    path('signup/', views.signup, name='home.html'),
    path('login/', views.handleLogin, name='login.html'),
    path('logout/', views.handleLogout, name='logout.html'),
]