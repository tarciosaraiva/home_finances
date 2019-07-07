from datetime import datetime
from pony.orm import *

db = Database()

class Budget(db.Entity):
    id = PrimaryKey(int, auto=True)
    user = Required('User')
    items = Set('Item')
    name = Required(str)
    preferred = Required(bool)
    created_at = Optional(datetime)


class Bucket(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    threshold = Optional(float)
    items = Set('Item')


class Category(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    items = Set('Item', cascade_delete=False)


class Account(db.Entity):
    id = PrimaryKey(int, auto=True)
    item_accounts = Set('ItemAccount')
    name = Required(str)
    number = Optional(str)
    branch = Optional(str)


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    email = Required(str)
    password = Required(str)
    budgets = Set(Budget)


class Item(db.Entity):
    id = PrimaryKey(int, auto=True)
    description = Required(str)
    category = Required(Category)
    item_accounts = Set('ItemAccount')
    bucket = Required(Bucket)
    budgets = Set(Budget)
    type = Required(str)  # income or expense
    frequency = Required(str)  # weekly, fortnightly, monthly, bimonthly, quarterly, annually
    amount = Required(float)


class ItemAccount(db.Entity):
    items = Required(Item)
    accounts = Required(Account)
    ratio = Required(float)
    PrimaryKey(items, accounts)

set_sql_debug(True)