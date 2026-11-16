from selenium import webdriver
from fixtures.session import SessionHelper
from fixtures.helper import GroupHelper
from fixtures.helper import ContactHelper

class Application:

    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url


    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
    def destroy(self):
        self.wd.quit()

