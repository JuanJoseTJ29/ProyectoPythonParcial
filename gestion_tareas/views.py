from django.shortcuts import render
from django.http import HttpResponse
from gestion_tareas.models import usuario, tarea
from django.http import HttpResponseRedirect
from django.urls import reverse
from dateutil.parser import parse


#Funcion para poder logearse
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
             return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
        else:
            return render(request,'gestion_tareas/ingresar.html',{
                'mensaje':'Los datos ingresados son incorrectos',
           })
    return render(request,'gestion_tareas/ingresar.html')

#Funcion para mostrar los datos en el dashboard
def dashboard(request):
    tareas_totales = tarea.objects.all()
    #Filtrar tareas propias
    tareas_propias=[]
    tareas_mias= tarea.objects.filter(usuario_responsable='juan')
    for tareas in tareas_mias:
        tareas_propias.append(tareas)

     #Filtrar finalizado
    return render(request, 'gestion_tareas/dashboard.html', {
        'objTarea':tareas_propias,
    })

#Funcion para crear una tarea
def nuevaTarea(request):
    if request.method == 'POST':
        nombreTarea=request.POST.get('nombreTarea')
        descripcionTarea=request.POST.get('descripcionTarea')
        fcTarea=request.POST.get('fcTarea')
        fcTarea=parse(fcTarea)
        feTarea=request.POST.get('feTarea')
        feTarea=parse(feTarea)
        usuarioTarea=request.POST.get('usuarioTarea')
        estadosTareas=request.POST.get('estadosTareas')
        tarea(nombre_tarea=nombreTarea,descripcion=descripcionTarea,fecha_creacion=fcTarea, fecha_entrega=feTarea , usuario_responsable=usuarioTarea, estadoTarea='PROGRESO').save()
        return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
    return render(request,'gestion_tareas/nuevaTarea.html',{
        'tareas_registradas':tarea.objects.all()
    })

#Funcion para editar una tarea
def editarTarea(request,ind):
    tarea_editar = tarea.objects.get(id=ind)
    if request.method == 'POST':
        nombreTarea=request.POST.get('nombreTarea')
        descripcionTarea=request.POST.get('descripcionTarea')
        fcTarea=request.POST.get('fcTarea')
        fcTarea=parse(fcTarea)
        feTarea=request.POST.get('feTarea')
        feTarea=parse(feTarea)
        usuarioTarea=request.POST.get('usuarioTarea')
        estadosTareas=request.POST.get('estadosTareas')    

        tarea_editar.nombre_tarea = nombreTarea
        tarea_editar.descripcion = descripcionTarea
        tarea_editar.fecha_creacion = fcTarea
        tarea_editar.fecha_entrega = feTarea
        tarea_editar.usuario_responsable= usuarioTarea
        tarea_editar.estadoTarea= estadosTareas
        tarea_editar.save()
        return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
    return render(request,'gestion_tareas/editarTarea.html',{
        'tarea_info' : tarea_editar,
        'tareas_registradas':tarea.objects.all()
    })

#Funcion para eliminar una tarea
def eliminarTarea(request,ind):
    tarea_eliminar = tarea.objects.get(id=ind)
    if request.method == 'POST':
        tarea_eliminar.delete()
        return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
    return render(request,'gestion_tareas/eliminarTarea.html',{
        'tarea_info' : tarea_eliminar,
        'tareas_registradas':tarea.objects.all()
    })

#Funcion para mostrar detalles de la tarea
def detalleTarea(request,ind):
 tareas_detalles = tarea.objects.get(id=ind)

 return render(request, 'gestion_tareas/detalleTarea.html', {
        'tareas_detalles': tareas_detalles,
    })

#Funcion para darle estado finalizado a una tarea
def finalizarTarea(request,ind):
    tarea_finalizar = tarea.objects.get(id=ind)
    if request.method == 'POST':
        estadosTareas=request.POST.get('estadosTareas')
        tarea_finalizar.estadoTarea= 'FINALIZADA'
        tarea_finalizar.save()
        return HttpResponseRedirect(reverse('gestion_tareas:dashboard'))
    return render(request,'gestion_tareas/finalizarTarea.html',{
        'tarea_finalizar' : tarea_finalizar,
        'tareas_registradas':tarea.objects.all()
    })
