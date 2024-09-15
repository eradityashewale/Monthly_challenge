from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    
    redirect_month = months[month-1]
    return HttpResponseRedirect("/challenges/" + redirect_month)
 
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("<h1>This month is not supported<h1/>")
    return HttpResponse (challenge_text)
 