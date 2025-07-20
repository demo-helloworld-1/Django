from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

from meetings.models import Meeting

def welcome(request):
    return render(request, "website/welcome.html",
                  {"num_meetings":Meeting.objects.count()})


def date(request):
    return HttpResponse("This session is serverd at " + str(datetime.now()))

def about(request):
    return HttpResponse("My Self Dhanush and I am writing Django Scripts")