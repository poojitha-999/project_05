from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    s="hey everyone "
    return HttpResponse(s)