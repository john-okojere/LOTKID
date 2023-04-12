from django.shortcuts import render, redirect
from django.conf import settings
from .models import Phone, Prayer
from django.contrib import messages



def home(request):
    print(settings.STATIC_ROOT)
    print(settings.STATIC_URL)
    return render(request, 'home.html', {})

def addphone(request):
    phone = request.POST.get('phone')
    phone = Phone.objects.create(phone=phone)
    messages.success(request, "Your phone number has been saved")
    return redirect('/')

def addprayer(request):
    name = request.POST.get('name')
    prayer = request.POST.get('prayer')
    prayer = Prayer.objects.create(name=name, prayer=prayer)
    messages.success(request, "Your request has been sent")
    return redirect('/')