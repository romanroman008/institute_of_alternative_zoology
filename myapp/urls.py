from django.urls import path

from myapp import views

app_name='myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.details, name='details'),
]