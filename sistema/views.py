import hashlib
from django.shortcuts import render
from datetime import datetime
from sistema.models import Usuario
from sistema.models import Paciente
from sistema.models import Historial
from sistema.models import Diagnostico
from sistema.models import Cama
#Ajax
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from sistema.serializers import PacienteSerializer

#-----------------------------AJAX-----------------------------
class PacienteGet(APIView):
    def get(self, request):
        pac = Paciente.objects.all().order_by('-id')[:3]
        ser = PacienteSerializer(pac, many = True)
        return Response(ser.data)

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
            tabla = " --- "
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
        
        # Se registra en la tabla historial.
        descripcion = "Cierra Sesión"
        tabla = " --- "
        fechayhora = datetime.now()
        usuario = request.session["idUsuario"]
        his = Historial(descripcion_historial=descripcion, tabla_afectada_historial=tabla, fecha_hora_historial=fechayhora, usuario_id=usuario)
        his.save()

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
    if request.method == "POST":
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
    
    else:
        datos = {
            'r' : 'Debe Presionar El Boton Para Registrar Un Proyecto!'
        }
        return render(request, 'registrar_proyecto.html', datos)

def listarPacientes(request):
    try:
        print("SESION:", request.session)
        estado = request.session['estadoSesion']
        nombre = request.session['nomUsuario']
        datos = {'nomUsuario':nombre}
        if estado is True:
            p = Paciente.objects.all().order_by('-id')
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

def mostrarActualizarPaciente(request, id):
    estadoSesion = request.session.get("estadoSesion")
    if estadoSesion is True:
        if request.session["nomUsuario"].upper() != "ADMIN":
            encontrado = Paciente.objects.get(id=id)
            p = Paciente.objects.all().values()

            datos = {
                'nomUsuario': request.session["nomUsuario"],
                'encontrado': encontrado,
                'paciente': p
            }
            return render(request, 'actualizar_paciente.html', datos)
        else:
            p = Paciente.objects.all().values()
            datos = {
                'nomUsuario': request.session["nomUsuario"],
                'paciente': p,
                'r': 'No Tiene Los Permisos Para Realizar La Acción!!'
            }
            return render(request, 'menu.html', datos)
    else:
        p = Paciente.objects.all().values()
        datos = {
            'nomUsuario': request.session.get("nomUsuario", ""),
            'paciente': p,
            'r': 'Debe Iniciar Sesión Para Acceder!!'
        }
        return render(request, 'index.html', datos)

def actualizarPaciente(request,id):
    estado = request.session['estadoSesion']
    nombre = request.session['nomUsuario']
    datos = {'nomUsuario':nombre}
    if estado is True:
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

        diag = Diagnostico.objects.filter(paciente_id=id).first()

        p = Paciente.objects.get(id=id)
        p.rut=rut
        p.prevision = pvs
        p.accidenteLaboral = acc
        p.genero = sex
        p.edad = eda
        p.Comobilidades = com
        p.funcionalidad = fun
        p.motivoDerivacion = der
        p.prestacionRequerida = pre
        p.evaluacion = eva
        p.adicional = inf
        p.save()

        # Se registra en la tabla historial.
        descripcion = "Actualización realizada (" + rut + ")"
        tabla = "Paciente"
        fechayhora = datetime.now()
        usuario = request.session["idUsuario"]
        his = Historial(
            descripcion_historial=descripcion,
            tabla_afectada_historial=tabla,
            fecha_hora_historial=fechayhora,
            usuario_id=usuario
        )
        his.save()

        p = Paciente.objects.get(id=id)
        datos = {
                'nomUsuario':nombre,
                'paciente':p,
                'diagnostico': diag
                }
        return render(request, 'ficha_paciente.html', datos)
    else:
        datos = {'r':'Debe iniciar sesión para ingresar al menu!'}
        return render(request,'index.html',datos)

def eliminarPaciente(request, id):
    try:
        estado = request.session['estadoSesion']
        nombre = request.session['nomUsuario']
        if estado is True and nombre == 'MEDICO':
            p = Paciente.objects.get(id=id)
            rut = p.rut
            p.delete()

            # Se registra en la tabla historial.
            descripcion = "Eliminación realizada (Rut:"+rut+")"
            tabla = "Paciente"
            fechayhora = datetime.now()
            usuario = request.session["idUsuario"]
            his = Historial(descripcion_historial=descripcion, tabla_afectada_historial=tabla, fecha_hora_historial=fechayhora, usuario_id=usuario)
            his.save()

            datos = {
                'nomUsuario' : request.session["nomUsuario"],  
                'r' : 'Paciente (Rut:'+ rut +') Eliminado Correctamente!'
            }
            
            return render(request, 'ficha_paciente.html', datos)
    except:
        datos = {
            'nomUsuario' : request.session["nomUsuario"], 
            'r' : 'El ID ('+str(id)+') No Existe. Imposible Eliminar!!'
        }
        return render(request, 'ficha_paciente.html', datos)

def mostrarFichaPaciente(request, id):
    try:
        estado = request.session['estadoSesion']
        nombre = request.session['nomUsuario']

        if estado is True:

            p = Paciente.objects.get(id=id)

            # Buscar diagnóstico asociado
            diagnostico = Diagnostico.objects.filter(paciente_id=id).last()

            datos = {
                'nomUsuario': nombre,
                'paciente': p,
                'diagnostico': diagnostico,  # <-- LO IMPORTANTE
            }

            return render(request, 'ficha_paciente.html', datos)

        else:
            datos = {'r': 'Debe iniciar sesión para ingresar al menu!'}
            return render(request, 'index.html', datos)

    except:
        datos = {'r': 'Debe iniciar sesión para ingresar al menu!'}
        return render(request, 'index.html', datos)

def solicitarDiagnostico(request,id):
    p = Paciente.objects.get(id=id)
    p.solicitudMedica = "SOLICITADO"
    p.save()
    
    ultimo = Diagnostico.objects.filter(paciente=p).order_by('-id').first()

    datos = {
            'paciente': p,
            'diagnostico': ultimo,
            'nomUsuario': request.session.get('nomUsuario', '')
        }

    return render(request, 'ficha_paciente.html', datos)

def ultimosPacientes(request):
    #Ajax
    datos = list(Paciente.objects.all().order_by('-id')[:5].values())
    return JsonResponse(datos, safe=False)

#-----------------------------CRUD DIAGNOSTICO-----------------------------
def insertarDiagnostico(request, id):
    estado = request.session['estadoSesion']
    nombre = request.session['nomUsuario']
    datos = {'nomUsuario':nombre}
    if estado is True:
        diag = request.POST['diagnostico']
        indi = request.POST['indicaciones']
        medi = request.POST['medicacion']

        p = Paciente.objects.get(id=id)

        d = Diagnostico(
        paciente     = p,
        diagnostico  = diag,
        medicacion   = medi,
        indicaciones = indi
        )
        
        p.solicitudMedica = "SIN_SOLICITUD"
        p.save()
        d.save()

        # Se registra en la tabla historial.
        descripcion = "Diagnostico realizado (Al Rut: " + p.rut + ")"
        tabla = "Diagnostico"
        fechayhora = datetime.now()
        usuario = request.session["idUsuario"]
        his = Historial(
            descripcion_historial=descripcion,
            tabla_afectada_historial=tabla,
            fecha_hora_historial=fechayhora,
            usuario_id=usuario
        )
        his.save()

        datos = {
                'nomUsuario':nombre,
                'paciente':p,
                'diagnostico':d,
                }
        return render(request, 'ficha_paciente.html', datos)
    else:
        datos = {'r':'Debe iniciar sesión para ingresar al menu!'}
        return render(request,'index.html',datos)

def actualizarDiagnostico(request, id):
    estado = request.session['estadoSesion']
    nombre = request.session['nomUsuario']

    if estado is True:
        diag = request.POST['diagnostico']
        medi = request.POST['medicacion']
        indi = request.POST['indicaciones']

        p = Paciente.objects.get(id=id)

        # Buscar último diagnóstico
        d = Diagnostico.objects.filter(paciente=p).order_by('-id').first()

        if d:  # si existe, actualizar
            d.diagnostico = diag
            d.medicacion = medi
            d.indicaciones = indi
            d.save()
            p.solicitudMedica = "SIN_SOLICITUD"
            p.save()
        else:  # si no existe, crear
            d = Diagnostico.objects.create(
                paciente=p,
                diagnostico=diag,
                medicacion=medi,
                indicaciones=indi
            )

        # registrar historial
        Historial.objects.create(
            descripcion_historial="Diagnóstico actualizado (Al Rut: " + p.rut + ")",
            tabla_afectada_historial="Diagnostico",
            fecha_hora_historial=datetime.now(),
            usuario_id=request.session["idUsuario"]
        )

        return render(request, 'ficha_paciente.html', {
            'nomUsuario': nombre,
            'paciente': p,
            'diagnostico': d,
        })

    return render(request,'index.html',{'r':'Debe iniciar sesión para ingresar al menu!'})

def eliminarDiagnostico(request):
    pass

#-----------------------------CRUD CAMAS-----------------------------

#-----------------------------VER HISTORIAL-----------------------------
def listarHistorial(request):
    try:
        print("SESION:", request.session)
        estado = request.session['estadoSesion']
        nombre = request.session['nomUsuario']
        if estado is True:
            h = Historial.objects.all().order_by('-id')
            datos = {'his': h,
                     'nomUsuario':nombre}
            return render(request, 'listar_historial.html', datos)
        else:
            datos = {'r':'Debe iniciar sesión para ingresar al menu!'}
            return render(request,'index.html',datos)
    except:
            datos = {'r':'Debe iniciar sesión para ingresar al menu!'}
            return render(request,'index.html',datos)

#-----------------------------FILTROS-----------------------------
def filtrarPacientes(request):
    estado = request.session.get('estadoSesion', False)
    nombre = request.session.get('nomUsuario', '')

    if not estado:
        return render(request,'index.html', {'r':'Debe Iniciar Sesión Para Acceder!!'})

    campo = request.POST.get('campo', 'todos')
    filtro = request.POST.get('txtfil', '').strip()

    pacientes = Paciente.objects.all()

    if campo != 'todos' and filtro:
        if campo == 'rut':
            pacientes = pacientes.filter(rut__icontains=filtro)
        elif campo == 'genero':
            pacientes = pacientes.filter(genero__icontains=filtro)
        elif campo == 'edad' and filtro.isdigit():
            pacientes = pacientes.filter(edad=int(filtro))

    return render(request, 'listar_pacientes.html', {
        'nomUsuario': nombre,
        'pacientes': pacientes,
        'campo_actual': campo,
        'filtro_actual': filtro,
    })
