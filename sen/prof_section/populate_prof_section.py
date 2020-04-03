import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sen.settings')

import django
django.setup()

#adding fake data

import random
from prof_section.models import AttendanceRecord,Prof
from faker import Faker

fake = Faker()

ids = ['201701131','201701130','201701138','201701133']
courses= ['IT413','CS203','HM413','IT303']
def  add_record():
	record = AttendanceRecord.objects.get_or_create(\
		student`ID=random.choice(ids), courseID=random.choice(courses))[0]
	record.save()
	return record

def populate(N=5):
	for entry in range(N):
		add_record()

if __name__=='__main__':
	print("Populating Prof_section!")
	populate()
	print("Complete!") 