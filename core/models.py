from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100,unique=True, error_messages={'unique':"This email has already been registered."})
    hobby = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name

