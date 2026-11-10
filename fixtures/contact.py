class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact_parameters):
        wd = self.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact_parameters.contact_firstname)
        wd.find_element_by_xpath("//body").click()
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact_parameters.mobile_phone)
        # submit contact creation
        wd.find_element_by_xpath("//input[19]").click()