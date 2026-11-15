# -*- coding: utf-8 -*-
import pytest
from models.contact import Contact
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", address="", mobile_phone="", home_phone="", work_phone="", email1="", email2="", email3="")] + [
Contact(firstname=random_string("firstname", 5), lastname=random_string("lastname", 10), address=random_string("address", 20), mobile_phone=random_string("mobile_phone", 10), home_phone=random_string("home_phone", 30), work_phone=random_string("work_phone", 40), email1=random_string("email1", 30), email2=random_string("email2", 20), email3=random_string("email3", 10))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
