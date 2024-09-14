from django import forms
from .models import Course, TutorProfile

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'duration', 'seats_available', 'details', 'tutor_id']
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'seats_available': forms.NumberInput(attrs={'class': 'form-control'}),
            'details': forms.TextInput(attrs={'class': 'form-control'}),
            'tutor_id': forms.NumberInput(attrs={'class': 'form-control'}),
        }
 
class TutorProfileForm(forms.ModelForm):
    class Meta:
        model = TutorProfile
        fields = ['name', 'email', 'courses']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'courses': forms.TextInput(attrs={'class': 'form-control'}),
        }