from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
monthly_challenges = {
    "january":"<h1>Eat no mea month !!!<h1/>",
    "february":"<h1>Walk for at least 20 minutes every day<h1/>",
    "march":"<h1>Learn Django for at least 20 minutes every day<h1/>",
    "april":"<h1>Eat no meat for the entire month<h1/>",
    "may":"<h1>Walk for at least 20 minutes every day<h1/>",
    "june":"<h1>Learn Django for at least 20 minutes every day<h1/>",
    "july":"<h1>Eat no meat for whole weak<h1/>",
    "august":"<h1>Auguest month Quate<h1/>",
    "september":"<h1>Septmeber Month of Ganapati<h1/>",
    "octomber":"<h1>Otomber Month Diwali<h1/>",
    "november":"<h1>November Month Entire weak",
    "december":"<h1Devemeber Month<h1/>"
}


def monthly_challenges(request, month):
    challenge_text = None
    if month == "january" or month == '1':
        challenge_text = "<h1>Eat no mea month !!!<h1/>"
    elif month == "february":
        challenge_text = ""
    elif month == "march":
        challenge_text = ""
    else:
        return HttpResponseNotFound("<h1>This month is not supported<h1/>")
    return HttpResponse (challenge_text)
 