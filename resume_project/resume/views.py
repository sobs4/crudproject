from django.shortcuts import render

# Create your views here.
from .models import Profile

def resume_view(request):
     profile = Profile.objects.first() # For simplicity, we'll just use the first profile
     return render(request, 'resume/resume.html', {'profile': profile})

