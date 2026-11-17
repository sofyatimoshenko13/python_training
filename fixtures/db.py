import pymysql.cursors
from models.group import Group
from models.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list;")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, mobile, home, work, email, email2, email3 from addressbook;")
            for row in cursor:
                (id, firstname, lastname, address, mobile_phone, home_phone, work_phone, email1, email2, email3) = row
                contact_list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, mobile_phone=mobile_phone, home_phone=home_phone, work_phone=work_phone, email1=email1, email2=email2, email3=email3))
        finally:
            cursor.close()
        return contact_list

    def destroy(self):
        self.connection.close()