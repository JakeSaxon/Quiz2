from selenium import webdriver
import unittest
import os

class HomePageTest(unittest.TestCase):

    def SetUp(self):
        if os.name=='nt'
            self.browser = webdriver.Chrome()

        else:
            self.browser = webdriver.Firefox()
