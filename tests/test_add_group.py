# -*- coding: utf-8 -*-
from models.group import Group


def test_add_group(app):
    app.group.create_group(Group(name="fgh", header="fgh", footer="fgh"))


def test_add_empty_group(app):
    app.group.create_group(Group(name="", header="", footer=""))