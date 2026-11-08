# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact_parameters import Contact
from application_for_contact import Application
from selenium.webdriver.chrome.webdriver import WebDriver


class TestAddNewContact(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_new_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(contact_firstname=u"РЎРѕС„СЊСЏ", mobile_phone="8974298546004"))
        self.app.logout()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()