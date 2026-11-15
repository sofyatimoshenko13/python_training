class Contact:

    def __init__(self, firstname=None, mobile_phone=None, id=None):
        self.firstname = firstname
        self.mobile_phone = mobile_phone
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return self.id == other.id and self.firstname == other.firstname