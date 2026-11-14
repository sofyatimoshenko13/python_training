from models.contact_parameters import Contact

def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(contact_firstname="updated", mobile_phone="88005553535"))
    app.session.logout()