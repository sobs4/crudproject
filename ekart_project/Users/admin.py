from django.contrib import admin

# Register your models here.
from .models import UserProfile,UserAccount

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserAccount)
