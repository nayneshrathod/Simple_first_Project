from django.db import models


# Create your models here.
class AllCourses(models.Model):
    coursename = models.CharField(max_length=200)
    insname = models.CharField(max_length=200)

    def __str__(self):
        return self.coursename


class details(models.Model):
    cours = models.ForeignKey(AllCourses, on_delete=models.CASCADE)

    def __str__(self):
        self.cours
