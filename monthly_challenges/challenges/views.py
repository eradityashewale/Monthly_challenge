from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def january(request):
    return HttpResponse ("<h1>Eat no meat for entire month !!!<h1/>")

def february(request):
    return HttpResponse ("<h1> Walk for at least 20 minutes every day!!!<h1/>")
