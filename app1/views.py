from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista1 (request):
    html="""
    <h1 Style="color:green">Hola Mundo</h1>
"""
    return HttpResponse(html)