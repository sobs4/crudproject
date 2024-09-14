from django.shortcuts import render,redirect, get_object_or_404
from .forms import StudentRegisteration
from .models import UserProfile

# Create your views here.
def add_show(request):
    if request.method == "POST":
        fm = StudentRegisteration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegisteration()# returns a blank form after saving.
    else:
        fm = StudentRegisteration()# If no record to show, returns a blank form.
    
    stud = UserProfile.objects.all()
    
    return render(request, 'enroll/addandshow.html', {'form':fm, 'student':stud})

def delete_data(request,id):
    if request.method=="POST":
        pi = UserProfile.objects.get(pk=id) # get the user profile by primary key.UserProfile.objects.get(pk=id)
        pi.delete()
    return redirect('/enroll')

def update_data(request,id):
    
    pi = UserProfile.objects.get(pk=id) # get the user profile by primary key.UserProfile.objects.get(pk=id)
    
    if request.method=="POST":
        
        fm = StudentRegisteration(request.POST, instance=pi) # Get the user profile by primary key

        if fm.is_valid():
            fm.save()   
    
            return redirect('/enroll')
            
    else:
        fm =  StudentRegisteration(instance=pi)
    
    return render(request, 'enroll/update.html', {'form': fm})
        # Redirect after successful update
   