from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request,'aboutpage.html')
def home(request):
    return render(request,'homepage.html')