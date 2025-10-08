from django.urls import path

from myapp import views

app_name='myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.details, name='details'),
    path('add/', views.CuriosityCreateView.as_view(), name='create_curiosity'),
    path('update/<int:pk>', views.CuriosityUpdateView.as_view(), name='update_curiosity'),
    path('delete/<int:pk>', views.CuriosityDeleteView.as_view(), name='delete_curiosity'),

]