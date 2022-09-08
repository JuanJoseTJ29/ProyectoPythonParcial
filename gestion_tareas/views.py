from django.shortcuts import render
from django.http import HttpResponse
from gestion_tareas.models import usuario

def index(request):
    return HttpResponse('Mi primera aplicacion web')

def hola(request):
    return HttpResponse('Esta es la ruta Hola') 

def hastaluego(request):
    return HttpResponse('ADIOSSSSSSSSSSSSSS') 

def ingresar(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        passwordUsuario = request.POST.get('passwordUsuario')
        usuario_registrado = 0
        usuarios_totales = usuario.objects.all()

        for usuarios in usuarios_totales:
          if usuarios.nombre == nombreUsuario and usuarios.contraseña == passwordUsuario:
             usuario_registrado = 1
        
        if usuario_registrado == 1:
            return render(request, 'gestion_tareas/dashboard.html')
        else:
            return render(request,'gestion_tareas/ingresar.html',{
                'mensaje':'Los datos ingresados son incorrectos',
           })
    return render(request,'gestion_tareas/ingresar.html')

def dashboard(request):
    return render(request, 'gestion_tareas/dashboard.html')



# Create your views here.
