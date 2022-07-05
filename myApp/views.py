import imp
from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def getProfile(request):
    profile = Profile.objects.all()
    return JsonResponse({"profiles": list(profile.values())})

def createProfile(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        phno = request.POST['phno']

        newProfile = Profile(name=name, age=age, phno=phno)
        newProfile.save()
        return HttpResponse('Profile created Successfully.')