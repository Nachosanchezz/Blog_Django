from django.shortcuts import render
from .models import Project

# Create your views here.

def portfolio(request):
    projects = Project.objects.all()
    return(request, "portfolio/portfolio.html", {'projects':projects})
