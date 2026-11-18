from models.contact import Contact
import random


def test_modify_some_contact(app, db, json_contacts):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    contact = json_contacts
    contact.id = old_contact.id
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(old_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
