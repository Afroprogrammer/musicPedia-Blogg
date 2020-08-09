from django.http import HttpResponse
from django.shortcuts import render


#a function that returns a sting when the homepage request is sent.
def homepage(request):
    return render(request,'homepage.html')


# a function that would run when a request is sent including this function name
def about(request):
    return render(request,'about.html')
    # return HttpResponse('about') #this function sends and http response when its called just a response no template 
