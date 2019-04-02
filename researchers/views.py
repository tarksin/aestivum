from django.shortcuts import render

from .models import Researcher

def home(request):
    researchers = Researcher.objects
    # researchers = [{'name':'Anita Churchstone, Ph.D.','organization':'Cold Spring Harbor Laboratory'},
    #                 {'name':'Carl Schmidt, Ph.D.'    ,'organization':'University of California at Davis'},
    #                 {'name':'Ahmed Carlotti, Ph.D.'  ,'organization':'Stowers Institute for Medical Research'},
    #               ] 

    return render(request, 'researchers/home.html', {'researchers':researchers})
