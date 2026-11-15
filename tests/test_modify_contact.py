from models.contact import Contact
from random import randrange


def test_modify_some_contact_firstname(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="updated")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count_contacts()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_first_contact_mobile_phone(app):
    #if app.contact.count_contacts() == 0:
    #    app.contact.create_contact(Contact(mobile_phone="1111111"))
    #old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(mobile_phone="88005553535"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)