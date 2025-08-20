from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    time_now = datetime.today().strftime('%d/%m/%Y, %H:%M:%S')
    return HttpResponse("Polls index here!  " + time_now)
