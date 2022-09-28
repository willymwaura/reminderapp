

from django.http import HttpResponse
from post.models import Feature
from django.shortcuts import render
from .models import Feature
from datetime import date, datetime


# Create your views here.
def notify(request):
    
    today=datetime.now()
    year=today.year
    day=today.day
    month=today.month
   #find the date that matches with "today"
    a=Feature.objects.filter(year=year,day=day,month=month)
    #after finding the date you can send an sms or email to user for remainder
    if a != None:
        return HttpResponse("no activity today")

   #if no date no response
    return HttpResponse("no activity today")




