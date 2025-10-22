from django.shortcuts import render
from sistema.models import Usuario
import hashlib

# LOGIN
#---------------------------------------------------------------------------------------
def index(request):
    return render(request,'index.html')

def iniciarSesion(request):
    if request.method == 'POST':
        nom = request.POST['nombre']
        con = request.POST['contraseña']
        has = hashlib.md5(con.encode('utf-8')).hexdigest()
        comprobar = Usuario.objects.filter(nombre=nom,contraseña=has)

        if comprobar:
            request.session['estadoSesion'] = True
            request.session['nomUsuario'] = nom.upper()
            datos = {'nomUsuario':nom.upper()}
            if nom.upper() == 'TENS':
                return render(request,'menu.html',datos)
            elif nom.upper() == 'ADMIN':
                return render(request,'menu.html',datos)
            elif nom.upper() == 'MEDICO':
                return render(request,'menu.html',datos)
            elif nom.upper() == 'PARAMEDICO':
                return render(request,'menu.html',datos)
            else:
                datos = {'r':'Error en el Usuario.'}
                return render(request,'index.html',datos)
        else:
            datos = {'r':'Error en el Usuario y/o contraseña.'}
            return render(request,'index.html',datos)
    else:
        datos = {'r':'No se puede procesar la solicitud, intente nuevamente.'}
        return render(request,'index.html',datos)

def menu(request):
    try:
        estado = request.session['estadoSesion']
        nombre = request.session['nomUsuario']
        datos = {'nomUsuario':nombre}
        if estado is True:
            return render(request,'menu.html',datos)
        else:
            datos = {'r':'Debe iniciar sesión para ingresar al menu!'}
            return render(request,'index.html',datos)
    except:
            datos = {'r':'Debe iniciar sesión para ingresar al menu!'}
            return render(request,'index.html',datos)

def cerrarSesion(request):
    try:
        del request.session['estadoSesion']
        del request.session['nomUsuario']
        
        datos = {'r':'Sesion cerrada correctamente!'}
        return render(request, 'index.html',datos)

    except:
        datos = {'r':'La sesión está cerrada!'}
        return render(request, 'index.html',datos)
    
# CRUD
#---------------------------------------------------------------------------------------

# CRUD - CAMAS
#---------------------------------------------------------------------------------------