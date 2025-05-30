from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home')
    , path('profile', views.profile, name='profile')
    , path('workshops', views.workshops, name='workshops')
    , path('physicsCorner', views.physicsCorner, name='physicsCorner')
    , path('contact', views.contact, name='contact')

    , path('achievements', views.achievements_home, name='achievements')
    , path('achievements/schools', views.achievements_schools, name='achievements_schools')
    , path('achievements/students', views.achievements_students, name='achievements_students')
]