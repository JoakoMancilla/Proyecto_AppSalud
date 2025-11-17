from django.contrib import admin
from django.urls import path
from sistema import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Login
    path('',views.index),
    path('login/',views.iniciarSesion),
    path('logout/',views.cerrarSesion),

    #Menu
    path('menu/',views.mostrarMenu),
    
    #Historial
    path('historial/', views.listarHistorial),

    #Pacientes
    path('registrarPaciente/',views.registrarPacientes),
    path('insertarPaciente/',views.insertarPaciente),
    path('listarPacientes/',views.listarPacientes),
    path('mostrarBuscarPaciente/',views.mostraraBuscarPaciente),

    #Diagnosticos
    path('registrarDiagnostico/', views.registrarDiagnostico),
    #path('insertarDiagnostico/', views),
    #path('listarDiagnostico/', views),

    #Camas
    #path('actualizarCamas/', views),
    #path('insertarCamas/', views),
    #path('listarCamas/', views),


]
