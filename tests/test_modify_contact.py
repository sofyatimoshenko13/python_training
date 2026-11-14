from models.contact import Contact


def test_modify_first_contact_firstname(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(firstname="updated"))

def test_modify_first_contact_mobile_phone(app):
    if app.contact.count_contacts() == 0:
        app.contact.create_contact(Contact(mobile_phone="1111111"))
    app.contact.modify_first_contact(Contact(mobile_phone="88005553535"))