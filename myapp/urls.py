from django.urls import path
from myapp import views

urlpatterns = [
  path('', views.index, name='index'),
  path('register', views.register, name='register'),
  path('login', views.login, name='login'),
  path('logout', views.logout, name='logout'),
  path('create', views.adicionarLance, name='adicionarLance'),
  path('update', views.editarLance, name='editarLance'),
  path('delete',views.deleteLance, name='deleteLance'),
]