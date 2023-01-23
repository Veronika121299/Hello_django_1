from django.http import HttpResponse
from django.shortcuts import render

def about(reqest):
    return render(reqest, 'about.html')
def home(reqest):
    return HttpResponse('This is my home')