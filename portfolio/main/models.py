from django.db import models

# Create your models here.
class Profile(models.Model):
    display_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='images/profile_pics/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.display_name or "My Profile"
    
class ProfileSection(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=100)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title}"
    
class ProfileField(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='fields')
    key = models.CharField(max_length=100)
    value = models.TextField()

    def __str__(self):
        return f"{self.key}"