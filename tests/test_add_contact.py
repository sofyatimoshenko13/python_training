# -*- coding: utf-8 -*-
from models.contact import Contact


def test_add_new_contact(app):
    app.contact.create_contact(Contact(firstname="random", mobile_phone="8974298546004"))


def test_add_empty_contact(app):
    app.contact.create_contact(Contact(firstname="", mobile_phone=""))