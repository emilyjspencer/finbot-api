from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
  if request.method == 'POST':
    return HttpResponse('post')
  elif request.method == 'GET':
    return HttpResponse("Hello, world. You're inside Django.")