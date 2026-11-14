from models.contact import Contact


def test_modify_first_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="updated"))
    app.session.logout()

def test_modify_first_contact_mobile_phone(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(mobile_phone="88005553535"))
    app.session.logout()