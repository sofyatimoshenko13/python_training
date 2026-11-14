from models.group_parameters import Group

def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="updated", header="111", footer="222"))
    app.session.logout()