from django.test import TestCase
from django.contrib.auth.models import User
import random
from prof_section.models import AttendanceRecord,Prof

# Create your tests here.



class AdminTestCase(TestCase):
    def setUp(self):
        admin=User.objects.create(is_active=True, \
        	is_staff=True,username="admin")
        

    def test_adminUser_is_active(self):
        """Admin user is still active and in staff"""
        admin = User.objects.get(username='admin')
        self.assertEqual(admin.is_active , True)
        self.assertEqual(admin.is_staff, True)


ids = ['201701131','201701130','201701138','201701133']
courses= ['IT413','CS203','HM413','IT303']
class AttendanceRecordTestCase(TestCase):
	def test_student_is_registered(self):
		"""Student is actually registered to take course"""

		student = AttendanceRecord.objects.get_or_create( \
		 	studentID=random.choice(ids),        \
		 	 courseID=random.choice(courses))[0]

		#self.assertContains(" ".join(ids),student.studentID)
		self.assertEqual(student.studentID in ids ,True)

	

