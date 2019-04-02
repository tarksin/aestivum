from django.shortcuts import render

from researchers.models import Researcher

def index(request):
    researchers = Researcher.objects  #.filter(featured=True)
    context = {'researchers': researchers}
    return render(request, 'pages/index.html', context) 

def about(request):
    return render(request, 'pages/about.html') 