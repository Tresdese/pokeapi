from django.shortcuts import render
from django.http import HttpResponse

httpres = HttpResponse

def saludo(req):

    return httpres('ola')

def adios(req):
    return httpres('ayooos')
