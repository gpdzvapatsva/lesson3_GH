from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'index.html')

def records(request):
    return render (request, 'records.html')
def contacts(request):
    return render (request, 'contact.html')