import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sen.settings')

import django
django.setup()

#adding fake data

import random
from prof_section.models import AttendanceRecord,Prof
from stu_section.models import StudentCourses
from django.contrib.auth.models import User
from faker import Faker

fake = Faker()

ids = ['201701131','201701130','201701138','201701133']
courses= ['IT413','CS203','HM413','IT303']
default_prof_password =['password']

def  add_attendance_record():
	student = random.choice(StudentCourses.objects.all())
	username = student.user.username
	courseIDs = student.courses.split(" ")

	record = AttendanceRecord.objects.get_or_create(
		studentID=username, courseID= random.choice(courseIDs))[0]
	record.save()
	return record

def populate_attendance(N=5):
	for entry in range(N):
		add_attendance_record()

def populate_profs(N=3):
	users = []
	#Create 3 users
	for _ in range(N):
		user = User(username=fake.name(),password = default_prof_password)
		users.append(user)
		user.save()

	#create 3 prof with related to users created above, add courses
	for i in range(N):
		prof = Prof(user=users[i],courses = courses[i])
		prof.save()


if __name__=='__main__':
	print("Populating attendance records!")
	populate_attendance()
	print("Complete!") 
	print("---------------------------------------")
	print("Populating Profs!")
	populate_profs()
	print("Complete!") 
	