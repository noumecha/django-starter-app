# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hellow world! I'm Django")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("This is the about page") 
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse("This is the contact page") 
    return render(request, 'contact.html')