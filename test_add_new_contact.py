# -*- coding: utf-8 -*-
import pytest
from contact_parameters import Contact
from application_for_contact import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(contact_firstname=u"РЎРѕС„СЊСЏ", mobile_phone="8974298546004"))
    app.logout()