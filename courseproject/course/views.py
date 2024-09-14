# from django.shortcuts import render

# # Create your views here.
# def learn_django(request):
    
#     cname = 'Django'
#     duration = '4 Months'
#     seats = 10
#     django_details = {'nm': cname, 'du': duration, 'st': seats}
# #     return render(request,'course/courseone.html', django_details)
# from django.shortcuts import render,redirect, get_object_or_404
# from .forms import Course
# from .models import TutorProfile

# # Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseForm, TutorProfileForm
from .models import Course, TutorProfile


# def index(request):
#     # Render a template or redirect to another view
#     return render(request, 'index.html')

def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_courses')
    else:
        form = CourseForm()
    return render(request, 'course/add_course.html', {'form': form})

def add_tutor(request):
    if request.method == "POST":
        form = TutorProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tutors')
    else:
        form = TutorProfileForm()
    return render(request, 'course/add_tutor.html', {'form': form})

def show_courses(request):
    courses = Course.objects.all()
    return render(request, 'course/show_courses.html', {'courses': courses})

def show_tutors(request):
    tutors = TutorProfile.objects.all()
    return render(request, 'course/show_tutors.html', {'tutors': tutors})

def search_courses(request):
    if 'course_name' in request.GET:
        course_name = request.GET['course_name']
        courses = Course.objects.filter(course_name__icontains=course_name)
    else:
        courses = Course.objects.all()
    return render(request, 'course/search_courses.html', {'courses': courses})