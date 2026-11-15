from models.contact import Contact


def test_modify_first_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count_contacts() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    contact = Contact(firstname="updated")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_first_contact_mobile_phone(app):
    #old_contacts = app.contact.get_contact_list()
    #if app.contact.count_contacts() == 0:
    #    app.contact.create_contact(Contact(mobile_phone="1111111"))
    #app.contact.modify_first_contact(Contact(mobile_phone="88005553535"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)