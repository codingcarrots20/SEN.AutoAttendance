from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
#model is basically a table

class AttendanceRecord(models.Model):
	#these are basically columns
    studentID = models.CharField(max_length=10)
    courseID = models.CharField(max_length=10)
    dateTime = models.DateTimeField(default = datetime.now, blank=True)

    def __str__(self):
    	return (self.studentID,self.courseID,self.dateTime)

class Prof(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        
    )
    courses = models.CharField(max_length=100)
    
    def __str__(self):
        return (self.user.username)