from models.contact import Contact
from models.group import Group
import random
from fixtures.orm import ORMFixture


def test_add_contact_to_group(app, db):
    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name="test"))

    groups = db.get_group_list()
    group = random.choice(groups)

    # Берем контакты, которые еще НЕ входят в выбранную группу
    contacts_not_in_group = orm.get_contacts_not_in_group(group)
    if len(contacts_not_in_group) == 0:
        app.contact.create_contact(Contact(firstname="test"))
        contacts_not_in_group = orm.get_contacts_not_in_group(group)

    contact = random.choice(contacts_not_in_group)
    old_contacts_in_group = orm.get_contacts_in_group(group)

    app.contact.add_contact_to_group(contact.id, group.id)

    new_contacts_in_group = orm.get_contacts_in_group(group)
    old_contacts_in_group.append(contact)

    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
