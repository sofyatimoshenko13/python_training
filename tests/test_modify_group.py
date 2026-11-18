from models.group import Group
import random


def test_modify_some_group(app, db, json_groups, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name="test"))
    old_groups = db.get_group_list()
    old_group = random.choice(old_groups)
    group = json_groups
    group.id = old_group.id
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    old_groups.remove(old_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
