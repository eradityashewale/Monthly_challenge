from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def february(request):
    return HttpResponse ("<h1> Walk for at least 20 minutes every day!!!<h1/>")

def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "<h1>Eat no mea month !!!<h1/>"
    elif month == "february":
        challenge_text = "<h1>Walk for at least 20 minutes every day<h1/>"
    elif month == "march":
        challenge_text = "<h1>Learn Django for at least 20 minutes every day<h1/>"
    else:
        return HttpResponseNotFound("<h1>This month is not supported<h1/>")
    return HttpResponse (challenge_text)
