from . import views
from django.urls import path

app_name = 'gestion_tareas'

urlpatterns = [
    path('',views.ingresar,name='ingresar'),
    path('dashboard',views.dashboard,name='dashboard'),

   # path('hola',views.hola,name='hola'),
   # path('hastaluego',views.hastaluego,name='hastaluego'),

]