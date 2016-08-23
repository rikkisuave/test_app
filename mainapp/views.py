from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #template=get_template('boottemp.html')
    return render(request,'boottemp2.html')
