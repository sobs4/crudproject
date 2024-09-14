from django.db import models

# Create your models here.
class Profile(models.Model):  
     name = models.CharField(max_length=100)
     email = models.EmailField()
     phone = models.CharField(max_length=15)
     address = models.TextField()
     summary = models.TextField()
     
     def __str__(Self):
        return f'{Self.name}'


 
class Experience(models.Model):
     profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences')
     job_title = models.CharField(max_length=100)
     company = models.CharField(max_length=100)
     start_date = models.DateField()
     end_date = models.DateField(blank=True, null=True)
     description = models.TextField()
 
     def __str__(Self):
        return f'{Self.job_title}'
   
class Education(models.Model):
     profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='educations')
     degree = models.CharField(max_length=100)
     institution = models.CharField(max_length=100)
     start_date = models.DateField()
     end_date = models.DateField(blank=True, null=True)
     
     def __str__(Self):
        return f'{Self.degree}'
 
class Skill(models.Model):
     profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
     name = models.CharField(max_length=100)
     
     def __str__(Self):
        return f'{Self.name}'
        return f'{Self.profile}'