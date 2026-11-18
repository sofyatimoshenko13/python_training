from models.contact import Contact
import random
import re


def test_modify_some_contact(app, db, json_contacts, check_ui):
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
    if check_ui:
        def clean(contact):
            return Contact(
                id=contact.id,
                firstname=re.sub(r"\s+", " ", contact.firstname).strip() if contact.firstname else "",
                lastname=re.sub(r"\s+", " ", contact.lastname).strip() if contact.lastname else "",
                address=re.sub(r"\s+", " ", contact.address).strip() if contact.address else "",
                all_phones=merge_phones_like_on_home_page(contact),
                all_emails=merge_emails_like_on_home_page(contact)
            )
        db_list = map(clean, new_contacts)
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: x.strip(),
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))