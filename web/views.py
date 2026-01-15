'''
Created on 3 Oca 2026

@author: burak
'''
from django.shortcuts import render

def home(request):
    return render(request, "web/home.html")

def about(request):
    return render(request, "web/about.html")

def projects(request):
    return render(request, "web/projects.html")

def contact(request):
    return render(request, "web/contact.html")

