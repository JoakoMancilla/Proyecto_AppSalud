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
    path('mostrarFichaPaciente/<int:id>',views.mostrarFichaPaciente),
    path('mostrarActualizarPaciente/<int:id>', views.mostrarActualizarPaciente),
    path('actualizarPaciente/<int:id>', views.actualizarPaciente),
    path('eliminarPaciente/<int:id>', views.eliminarPaciente),
    #ajax
    path('api/paciente/', views.PacienteGet.as_view()),

    #Diagnosticos
    path('registrarDiagnostico/<int:id>', views.insertarDiagnostico),
    path('actualizarDiagnostico/<int:id>', views.actualizarDiagnostico),
    path('solicitarDiagnostico/<int:id>', views.solicitarDiagnostico),

    #Camas
    path('mostrarActualizarCamas/', views.mostrarActulizarCamas),
    #ajax
    path('api/cama/', views.CamaGetPost.as_view()),
    path('api/cama/<int:id>', views.CamaGetPutDelete.as_view()),

    #Filtros
    path('filtrarPacientes/', views.filtrarPacientes)


]
