from django.shortcuts import render
from .models import Projects

# Create your views here.
def earth(request):
    projs = Projects.objects.all()
    return render(request,'earth.html',{'projs':projs})