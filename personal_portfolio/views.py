from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def home(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request, 'personal_portfolio/home.html', context)



