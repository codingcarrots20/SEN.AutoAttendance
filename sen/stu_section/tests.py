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

	

# Selenium Tests
from django.test import LiveServerTestCase
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ProfLoginTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox(executable_path="C:\\Users\\Mukund Kalra\\Downloads\\web-driver\\geckodriver")
        super(ProfLoginTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(ProfLoginTestCase, self).tearDown()

    def test_prof_login(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/prof_section/')

        #find the form element
        username = selenium.find_element_by_id('id_username')  
        password = selenium.find_element_by_id('id_password')
        submit = selenium.find_element_by_class_name('btn')


        #Fill the form with data
        username.send_keys('mukund')
        password.send_keys('password')
        

        #submitting the form
        submit.click()	


        #check the returned result
        assert selenium.title== 'Prof_page'