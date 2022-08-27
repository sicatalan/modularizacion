from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse("Funciona correctamente")

def create(request):
    return HttpResponse("Route to test the creation of data")