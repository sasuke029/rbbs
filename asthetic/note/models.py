from django.db import models
from django.contrib.auth.models import User





class Note(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


    

class Department(models.Model):
    name=models.CharField(max_length=100)


class Semester(models.Model):
    department = models.ForeignKey(Department , on_delete=models.CASCADE)
    name=models.CharField(max_length=100)


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Note, on_delete=models.SET_NULL, null=True)
    semester= models.ForeignKey(Semester, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, default="avatar.svg")
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name



    
class cart(models.Model):
    Subjects = models.CharField(max_length=100)
    Rate = models.PositiveIntegerField() 
    Quantity = models.PositiveIntegerField()
    Total_Price =models.PositiveIntegerField()

