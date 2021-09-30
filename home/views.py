from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Index
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request , 'index.html')

def submit(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        index = Index (name = name , email= email , desc=desc, date= datetime.today() )
        index.save()
        messages.success(request, 'Your message has been sent.')
    return render(request , 'index.html')

