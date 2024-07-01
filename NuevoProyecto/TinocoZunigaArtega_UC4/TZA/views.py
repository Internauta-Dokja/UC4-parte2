from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    
    return render(request, 'index.html')

def saludo(request):
    
    return render(request, 'saludo.html')




        







        
