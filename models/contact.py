from sys import maxsize

class Contact:

    def __init__(self, lastname = None, firstname=None,
                 all_phones_from_home_page = None, mobile_phone=None, home_phone=None, work_phone=None,
                 id=None):
        self.lastname = lastname
        self.firstname = firstname
        self.all_phones_from_home_page = all_phones_from_home_page
        self.mobile_phone = mobile_phone
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) and (self.firstname is None or other.firstname is None or self.firstname == other.firstname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
