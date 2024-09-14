from django.contrib import admin

# Register your models here.
from resume.models import Profile, Experience, Education, Skill

admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)