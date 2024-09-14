from django.db import models

# Create your models here.

class TutorProfile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    courses = models.ManyToManyField('Course', related_name='tutors')  # Many-to-many relationship with Course

    def __str__(self):
        return self.name

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    seats_available = models.IntegerField()
    details = models.CharField(max_length=100)
    tutor_id = models.IntegerField()
    def __str__(self):
        return self.course_name

    