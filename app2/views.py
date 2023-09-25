from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista2(request):
    html= """<p Style="color:red">Lorem Ipsum es el término para referirnos a un texto falso que simula caracteres latinos y que utilizamos para ver de un modo rápido cómo quedaría una página con el contenido; antes de tener el texto definitivo, para componer fácilmente la maqueta</p>
"""
    return HttpResponse(html)