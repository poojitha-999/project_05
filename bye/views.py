from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def clg(request):
    p="thanks for attending"
    return HttpResponse(p)
# Create your views here.
