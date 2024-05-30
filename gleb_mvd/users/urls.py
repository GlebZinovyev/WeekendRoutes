# Импортируем из приложения django.contrib.auth нужный view-класс
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('logout/', views.logout, name = 'logout'),
    # path(
    #   'logout/',
    #   LogoutView.as_view(template_name='users/logout.html'),
    #   name='logout'
    # ),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
] 