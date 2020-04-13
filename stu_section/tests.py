from django.test import TestCase
from django.contrib.auth.models import User
import random
from faker import Faker
from prof_section.models import AttendanceRecord, Prof
from stu_section.models import Student
# Create your tests here.

courses = ['IT413', 'CS203', 'HM413', 'IT303', 'EL203', 'MU12', 'OP125']
faker = Faker()

# Selenium Tests
from django.test import LiveServerTestCase
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class StudentLoginTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox(executable_path=".\\geckodriver")
        super(StudentLoginTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(StudentLoginTestCase, self).tearDown()

    def test_prof_login(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/stu_section/')

        #find the form element
        username = selenium.find_element_by_id('id_username')  
        password = selenium.find_element_by_id('id_password')
        submit = selenium.find_element_by_class_name('btn')


        #Fill the form with data
        username.send_keys('admin')
        password.send_keys('admin')
        

        #submitting the form
        submit.click()	


        #check the returned result
        assert selenium.title== 'Document'	


#Unit Test Cases
class AdminTestCase(TestCase):
	def setUp(self):
		admin = User.objects.create(is_active=True,
			is_staff=True, username="admin")

	def test_adminUser_is_active(self):
		"""Admin user is still active and in staff"""
		admin = User.objects.get(username='admin')
		self.assertEqual(admin.is_active, True)
		self.assertEqual(admin.is_staff, True)


# class AttendanceRecordTestCase(TestCase):
# 	name = faker.name()
# 	course = random.choice(courses)
# 	user = User(username=name, password=faker.password())
# 	user.save()

# 	def setUp(self):

# 		student = Student(user=self.user, courses=self.course)
# 		student.save()
# 		record = AttendanceRecord(studentID=self.name, courseID=self.course)
# 		record.save()

# 	def test_student_is_registered(self):
# 		"""Student is actually registered to take course"""
		
# 		# self.assertContains(" ".join(ids),student.studentID)

# 		student = Student.objects.get(user = self.user, courses=course)
# 		attendance_record = AttendanceRecord.objects.get(studentID= self.name, courseID=course)
# 		self.assertEqual(attendance_record.courseID in student.courses ,True)




		
	

