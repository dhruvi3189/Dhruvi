from django.shortcuts import render

from django.http import HttpResponse
def index(request):
      return HttpResponse('hello I am in second app')

# Create your views here.
