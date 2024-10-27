#Views.py
from django.http import HttpResponse
import datetime

def saludo(request): #Primera Vista
    return HttpResponse("Hola Alexis")

def despedida(request):
    return HttpResponse("Chao Alexis")

def dameFecha(request):
    fechaActual= datetime.datetime.now();
    
    documentoHtml="""
    <html>
    <body>
    <h1>
    Fecha y Hora: %s
    </h1>
    </body>
    </html>
    """ % fechaActual
    
    return HttpResponse(documentoHtml)

def calculaEdad(request,anio):
    edadActual = datetime.datetime.today().year - anio
    documentoHtml="""
    <html>
    <body>
    <h1>
    Tu edad: %s
    </h1>
    </body>
    </html>
    """ %(edadActual)
    return HttpResponse (documentoHtml)
