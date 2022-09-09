from . import views
from django.urls import path

app_name = 'gestion_tareas'

urlpatterns = [
    path('',views.ingresar,name='ingresar'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('nuevaTarea',views.nuevaTarea,name='nuevaTarea'),
    path('editarTarea/<str:ind>',views.editarTarea,name='editarTarea'),
    path('eliminarTarea/<str:ind>',views.eliminarTarea,name='eliminarTarea'),
    path('detalleTarea/<str:ind>',views.detalleTarea,name='detalleTarea'),

   # path('hola',views.hola,name='hola'),
   # path('hastaluego',views.hastaluego,name='hastaluego'),

]