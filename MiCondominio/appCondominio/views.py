from django.shortcuts import render
from django.http import HttpResponse
from .models import Casa, Condominio, Espacios_comunes, Usuario, Seguridad

# Create your views here.

def home(request):
    try:
        try:
            if request.GET["loggedin"]:
                loggedin = request.GET["loggedin"]
                #peliculas = Pelicula.objects.all()
                #generos = Genero.objects.all()
                context= {'loggedin':loggedin}
                return render(request, "home.html", context)
        except:
            return login(request)
    except:
        mensaje = "Problemas de carga en el home."
        return HttpResponse(mensaje)

def login(request):
    try:
        #if request.GET["loggedin"]:
         #   loggedin = request.GET["loggedin"]
          #  return home(request)
        #else: 
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