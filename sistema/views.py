import hashlib
from django.shortcuts import render
from datetime import datetime
from sistema.models import Usuario
from sistema.models import Paciente
from sistema.models import Historial
from sistema.models import Cama

#-----------------------------TEMPLATES-----------------------------
def index(request):
    return render(request,'index.html')

def iniciarSesion(request):
    if request.method == 'POST':
        nom = request.POST['nombre']
        con = request.POST['contraseña']
        has = hashlib.md5(con.encode('utf-8')).hexdigest()

        comprobar = Usuario.objects.filter(nombre=nom,contraseña=has).values()

        if comprobar:
            request.session['estadoSesion'] = True
            request.session['idUsuario'] = comprobar[0]['id']
            request.session['nomUsuario'] = nom.upper()

            datos = {'nomUsuario':nom.upper()}

            # Se registra en la tabla historial.
            descripcion = "Inicia Sesión"
            tabla = ""
            fechayhora = datetime.now()
            usuario = request.session["idUsuario"]
            his = Historial(descripcion_historial=descripcion, tabla_afectada_historial=tabla, fecha_hora_historial=fechayhora, usuario_id=usuario)
            his.save()

            if nom.upper() == 'TENS':
                return render(request,'menu.html',datos)
            elif nom.upper() == 'ADMIN':
                return render(request,'menu.html',datos)
            elif nom.upper() == 'MEDICO':
                return render(request,'menu.html',datos)
            elif nom.upper() == 'ENFERMERO':
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

def mostrarMenu(request):
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

#-----------------------------CRUD PACIENTES-----------------------------
def registrarPacientes(request):
    try:
        estado = request.session['estadoSesion']
        nombre = request.session['nomUsuario']
        datos = {'nomUsuario':nombre}
        if estado is True:
            return render(request,'registrar_paciente.html',datos)
        else:
            datos = {'r':'Debe iniciar sesión para ingresar al menu!'}
            return render(request,'index.html',datos)
    except:
            datos = {'r':'Debe iniciar sesión para ingresar al menu!'}
            return render(request,'index.html',datos)

def insertarPaciente(request):
    rut = request.POST['txtrut']
    pvs = request.POST['cbopvs']
    acc = request.POST['cboacc']
    sex = request.POST['cbosex']
    eda = request.POST['txteda']
    com = request.POST['txtcom']
    fun = request.POST['txtfun']
    der = request.POST['txtder']
    pre = request.POST['txtpre']
    eva = request.POST['txteva']
    inf = request.POST['txtinf']

    p = Paciente(rut=rut, prevision = pvs, accidenteLaboral = acc, genero = sex, edad = eda,
                Comobilidades = com, funcionalidad = fun, motivoDerivacion = der,
                prestacionRequerida = pre, evaluacion = eva, adicional = inf)
    
    p.save()
    respuesta = {'r':'Datos Guardados Correctamente!'}

    # Se registra en la tabla historial.
    descripcion = "Insert realizado ("+str(rut.lower())+")"
    tabla = "Pacientes"
    fechayhora = datetime.now()
    usuario = request.session["idUsuario"]
    his = Historial(descripcion_historial=descripcion, tabla_afectada_historial=tabla, fecha_hora_historial=fechayhora, usuario_id=usuario)
    his.save()

    return render(request, 'registrar_paciente.html', respuesta)

def listarPacientes(request):
    try:
        print("SESION:", request.session)
        print('Hola Mundo')
        estado = request.session['estadoSesion']
        nombre = request.session['nomUsuario']
        datos = {'nomUsuario':nombre}
        if estado is True:
            p = Paciente.objects.all()
            datos = {
                'nomUsuario':nombre,
                'pacientes':p
                }
            return render(request,'listar_pacientes.html',datos)
        else:
            datos = {'r':'Debe iniciar sesión para ingresar al menu!'}
            return render(request,'index.html',datos)
    except:
            datos = {'r':'Debe iniciar sesión para ingresar al menu!'}
            return render(request,'index.html',datos)

def actualizarPacientes(request):
    pass

def eliminarPacientes(request):
    pass

def mostraraBuscarPaciente(request):
    return render(request, 'buscar_paciente.html')

def buscarPaciente(request):
    pass
#-----------------------------CRUD DIAGNOSTICO-----------------------------
def registrarDiagnostico(request):
    try:
        estado = request.session['estadoSesion']
        nombre = request.session['nomUsuario']
        datos = {'nomUsuario':nombre}
        if estado is True:
            return render(request,'registrar_diagnostico.html',datos)
        else:
            datos = {'r':'Debe iniciar sesión para ingresar al menu!'}
            return render(request,'index.html',datos)
    except:
            datos = {'r':'Debe iniciar sesión para ingresar al menu!'}
            return render(request,'index.html',datos)

def insertarDiagnostico(request):
    pass

def listarDiagnosticos(reuqest):
    pass

def actualizarDiagnostico(request):
    pass

def eliminarDiagnostico(request):
    pass

#-----------------------------CRUD CAMAS-----------------------------

#-----------------------------VER HISTORIAL-----------------------------
def listarHistorial(request):
    try:
        print("SESION:", request.session)
        print('Hola Mundo')
        estado = request.session['estadoSesion']
        nombre = request.session['nomUsuario']
        datos = {'nomUsuario':nombre}
        if estado is True:
            h = Historial.objects.all()
            datos = {'his': h}
            return render(request, 'listar_historial.html', datos)
        else:
            datos = {'r':'Debe iniciar sesión para ingresar al menu!'}
            return render(request,'index.html',datos)
    except:
            datos = {'r':'Debe iniciar sesión para ingresar al menu!'}
            return render(request,'index.html',datos)

#-----------------------------FILTROS-----------------------------
