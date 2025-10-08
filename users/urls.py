from django.urls import path

from users import views
from django.contrib.auth import views as auth_views

from users.forms import LoginForm

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm,template_name='users/login.html'), name='login' ),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
]