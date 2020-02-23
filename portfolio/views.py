from django.shortcuts import render
from .models import Project


# Create your views here.
def home(request):
    """
    A view that gets all the objects in the
    Project table, renders the home.html
    template and injects the projects into it
    """
    projects = Project.objects.all()

    context = {
        'projects': projects
    }

    return render(request, 'home.html', context)
