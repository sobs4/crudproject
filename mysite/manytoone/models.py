from django.db import models

# Create your models here.
#To define a many-to-one relationship, use ForeignKey.

#In this example, a Reporter can be associated with many Article objects, but an Article can only have one Reporter object:


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    #class Meta:
     #   ordering = ["headline"]