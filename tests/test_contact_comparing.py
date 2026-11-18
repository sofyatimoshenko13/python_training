import re
from models.contact import Contact


def test_parameters_on_home_page(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contacts_from_home_page)):
        home_contact = contacts_from_home_page[i]
        db_contact = contacts_from_db[i]
        assert home_contact.firstname == (db_contact.firstname.strip() if db_contact.firstname else "")
        assert home_contact.lastname == (db_contact.lastname.strip() if db_contact.lastname else "")
        assert home_contact.address == (db_contact.address.strip() if db_contact.address else "")
        assert home_contact.all_phones == merge_phones_like_on_home_page(db_contact)
        assert home_contact.all_emails == merge_emails_like_on_home_page(db_contact)


def clear(s):
    return re.sub("[/() .-]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map (lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                        [contact.home_phone, contact.mobile_phone, contact.work_phone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                 filter(lambda x: x is not None,
                                        [contact.email1, contact.email2, contact.email3])))

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert merge_phones_like_on_home_page(contact_from_view_page) == merge_phones_like_on_home_page(contact_from_edit_page)

def test_emails_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_emails == merge_emails_like_on_home_page(contact_from_edit_page)

def test_name_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname

def test_address_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.address == contact_from_edit_page.address
