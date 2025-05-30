from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def profile(request):
    return render(request, 'main/profile.html')

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