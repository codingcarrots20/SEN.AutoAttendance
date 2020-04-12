import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sen.settings')

import django
django.setup()

import random
from prof_section.models import AttendanceRecord,Prof
from stu_section.models import StudentCourses
from django.contrib.auth.models import User
from faker import Faker

fake = Faker()

ids = ['201701131','201701130','201701138','201701133']
courses= ['IT413','CS203','HM413','IT303','EL203','MU12', 'OP125']
default_stud_password =['password']


def populate_students_courses(N=3):
	users = []
	#Create 3 users
	for _ in range(N):
		user = User(username=fake.name(),password = default_stud_password)
		users.append(user)
		user.save()

	#create 3 prof with related to users created above, add courses
	for i in range(N):
		stud = StudentCourses(user=users[i],courses = random.choice(courses))
		stud.save()


if __name__=='__main__':
	print("Populating Student records!")
	populate_students_courses()
	print("Complete!") 
	print("---------------------------------------")
	