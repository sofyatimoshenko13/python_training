from models.contact import Contact


def test_modify_first_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="updated"))

def test_modify_first_contact_mobile_phone(app):
    app.contact.modify_first_contact(Contact(mobile_phone="88005553535"))