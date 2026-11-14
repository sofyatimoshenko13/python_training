# -*- coding: utf-8 -*-
import pytest
from models.contact_parameters import Contact
from fixtures.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(contact_firstname=u"РЎРѕС„СЊСЏ", mobile_phone="8974298546004"))
    app.session.logout()