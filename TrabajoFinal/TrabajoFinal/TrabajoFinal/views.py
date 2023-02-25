from django.http import HttpResponse
from django.template import Template, Context
import random



def registarse(request):
   
    mihtml = open("C:/Users/pollo/OneDrive/Desktop/TrabajoFinal/TrabajoFinal/TrabajoFinal/plantillas/registrarse.html")       

    plantillas = Template(mihtml.read())

    mihtml.close()

    micontexto = Context()

    documento = plantillas.render(micontexto)
    
    return HttpResponse(documento)


def peliculas(request):
   
    mihtml = open("C:/Users/pollo/OneDrive/Desktop/TrabajoFinal/TrabajoFinal/TrabajoFinal/plantillas/peliculas.html")       

    plantillas = Template(mihtml.read())

    mihtml.close()

    micontexto = Context()

    documento = plantillas.render(micontexto)
    
    return HttpResponse(documento)

def loqueseviene(request):
   
    mihtml = open("C:/Users/pollo/OneDrive/Desktop/TrabajoFinal/TrabajoFinal/TrabajoFinal/plantillas/loqueseviene.html")       

    plantillas = Template(mihtml.read())

    mihtml.close()

    micontexto = Context()

    documento = plantillas.render(micontexto)
    
    return HttpResponse(documento)


def iniciarsesion(request):
   
    mihtml = open("C:/Users/pollo/OneDrive/Desktop/TrabajoFinal/TrabajoFinal/TrabajoFinal/plantillas/iniciarsesion.html")       

    plantillas = Template(mihtml.read())

    mihtml.close()

    micontexto = Context()

    documento = plantillas.render(micontexto)
    
    return HttpResponse(documento)     

def mi_pagina(request):
   
    mihtml = open("C:/Users/pollo/OneDrive/Desktop/TrabajoFinal/TrabajoFinal/TrabajoFinal/plantillas/index.html")       

    plantillas = Template(mihtml.read())

    mihtml.close()

    micontexto = Context()

    documento = plantillas.render(micontexto)
    
    return HttpResponse(documento)