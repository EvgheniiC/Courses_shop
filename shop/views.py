from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hallo from shop app")
