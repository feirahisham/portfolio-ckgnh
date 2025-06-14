from django.contrib import admin
from .models import Profile, ProfileSection, ProfileField

# Register your models here.
admin.site.register(Profile)
admin.site.register(ProfileSection)
admin.site.register(ProfileField)