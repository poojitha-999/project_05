from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    s="hey everyone"
    return HttpResponse(s)