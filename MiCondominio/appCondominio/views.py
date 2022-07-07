from django.shortcuts import render
from django.http import HttpResponse
from .models import Casa, Condominio, Espacios_comunes, Usuario, Seguridad
import requests

# Create your views here.

def home(request):
    try:
        try:
            
            loggedin = request.GET["loggedin"]
            correo = request.GET["correo"]
            contrasena = request.GET["contrasena"]
            
            #seguridad = Seguridad.objects.filter(correo__icontains=correo,contrasena__icontains=contrasena)
            usuarios = Usuario.objects.all

            try:
                #usuario = Usuario.objects.filter(correo__icontains=correo)
                context= {'usuarios':usuarios,'loggedin':loggedin,'correo':correo}
                return render(request, "home.html", context)

            except:
                mensaje = "Usuario no registrado o no habilitado."
                #context = {'mensaje':mensaje}
                #return render(request,"login.html",context)
                return HttpResponse(mensaje)
        except:
            mensaje = "ruta inválida"
            #return login(request)
            return HttpResponse(mensaje)
    except:
        mensaje = "Problemas de carga en el home."

        context = {'mensaje':mensaje}
        return render(request,"login.html",context)
        #return HttpResponse(mensaje)

def login(request):
    try:
        try:
            mensaje = request.GET["mensaje"]
            context = {'mensaje':mensaje}
            return render(request, "login.html",mensaje)
        #if request.GET["loggedin"]:
         #   loggedin = request.GET["loggedin"]
          #  return home(request)
        #else:
        except:
            return render(request, "login.html")

    except:
        mensaje = "Problemas de carga en el login."
        return HttpResponse(mensaje)

def index(request):
    try:
    #if request.GET["loggedin"]:
         #   loggedin = request.GET["loggedin"]
          #  return home(request)
        #else: 
        return render(request, "login.html")

    except:
        mensaje = "Problemas de carga en el login."
        return HttpResponse(mensaje)

def registro(request):
    try:
    #if request.GET["loggedin"]:
         #   loggedin = request.GET["loggedin"]
          #  return home(request)
        #else: 
        return render(request, "registro.html")

    except:
        mensaje = "Problemas de carga en el registro."
        return HttpResponse(mensaje)


# Create your views here.
def users(request):
    #pull data from third party rest api
    response = requests.get('http://127.0.0.1:8000//usuarios')
    #convert reponse data into json
    users = response.json()
    print(users)
    return HttpResponse("Users")
    pass    

