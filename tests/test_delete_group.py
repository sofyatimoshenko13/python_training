from models.group import Group


def test_delete_first_group(app):
    if app.group.count_groups() == 0:
        app.group.create_group(Group(name="test"))
    app.group.delete_first_group()
