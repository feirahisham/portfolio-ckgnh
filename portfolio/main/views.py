from django.shortcuts import render
from .models import Profile, ProfileSection

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def profile(request):
    profile = Profile.objects.first()
    sections = ProfileSection.objects.prefetch_related('sections', 'fields').first()
    return render(request, 'main/profile.html', {
        'profile': profile
    })

def workshops(request):
    return render(request, 'main/workshops.html')

def physicsCorner(request):
    return render(request, 'main/physicsCorner.html')

def contact(request):
    return render(request, 'main/contact.html')

def achievements_home(request):
    return render(request, 'main/achievements/home.html')

def achievements_schools(request):
    return render(request, 'main/achievements/schools.html')

def achievements_students(request):
    return render(request, 'main/achievements/students.html')