from django.contrib import admin
from .models import TutorialGroup,Tutorial,UserProfile

# Register your models here.

admin.site.register(TutorialGroup)
admin.site.register(Tutorial)
admin.site.register(UserProfile)