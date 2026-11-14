from selenium.webdriver.chrome.webdriver import WebDriver
from fixtures.session import SessionHelper
from fixtures.helper import Helper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = Helper(self)
        self.contact = Helper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
    def destroy(self):
        self.wd.quit()

