from django.shortcuts import render, get_object_or_404

from .models import Researcher

def researchers(request):
    researchers = Researcher.objects
    # researchers = [{'name':'Anita Churchstone, Ph.D.','organization':'Cold Spring Harbor Laboratory'},
    #                 {'name':'Carl Schmidt, Ph.D.'    ,'organization':'University of California at Davis'},
    #                 {'name':'Ahmed Carlotti, Ph.D.'  ,'organization':'Stowers Institute for Medical Research'},
    #               ] 

    return render(request, 'researchers/researchers.html', {'researchers':researchers})


def researcher(request, researcher_id):
    researcher = get_object_or_404(Researcher, pk=researcher_id)
    # blog = {"title":"Really cool article"}
    return render(request, 'researchers/researcher.html', {'researcher':researcher})    
