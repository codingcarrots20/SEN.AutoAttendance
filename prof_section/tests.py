from django.test import TestCase

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