# -*- coding: utf-8 -*-
from models.contact_parameters import Contact


def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(contact_firstname=u"РЎРѕС„СЊСЏ", mobile_phone="8974298546004"))
    app.session.logout()