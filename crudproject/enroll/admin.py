from django.contrib import admin

# Register your models here.
from enroll.models import UserProfile

#admin.site.register(UserProfile)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id","name","email","password")