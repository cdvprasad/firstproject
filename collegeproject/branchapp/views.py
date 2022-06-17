from django.shortcuts import render
from .models import *
# Create your views here.

def view(request):
    data = StudentInfo.objects.all()
    return render(request,'branchapp/first.html',{'data':data})

