from models.contact import Contact
import random
import string


constant = [
    Contact(firstname="firstname1", lastname="lastname1", address="address1", mobile_phone="mobile_phone1", home_phone="home_phone1", work_phone="work_phone1", email1="email1_1", email2="email2_1", email3="email3_1"),
    Contact(firstname="firstname2", lastname="lastname2", address="address2", mobile_phone="mobile_phone2", home_phone="home_phone2", work_phone="work_phone2", email1="email1_2", email2="email2_2", email3="email3_2")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", address="", mobile_phone="", home_phone="", work_phone="", email1="", email2="", email3="")] + [
Contact(firstname=random_string("firstname", 5), lastname=random_string("lastname", 10), address=random_string("address", 20), mobile_phone=random_string("mobile_phone", 10), home_phone=random_string("home_phone", 30), work_phone=random_string("work_phone", 40), email1=random_string("email1", 30), email2=random_string("email2", 20), email3=random_string("email3", 10))
    for i in range(5)
]
