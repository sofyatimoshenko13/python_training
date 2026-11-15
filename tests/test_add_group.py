# -*- coding: utf-8 -*-
from models.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_group(Group(name="fgh", header="fgh", footer="fgh"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_group(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)