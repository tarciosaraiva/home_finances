from datetime import datetime
from pony.orm import *


db = Database()


class Budget(db.Entity):
    _table_ = 'budgets'
    id = PrimaryKey(int, auto=True)
    user = Required('User')
    name = Required(str)
    preferred = Required(bool)
    created_at = Optional(datetime)
    budget_items = Set('BudgetItem')


class Bucket(db.Entity):
    _table_ = 'buckets'
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    threshold = Optional(float)
    items = Set('Item')


class Category(db.Entity):
    _table_ = 'categories'
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    items = Set('Item', cascade_delete=False)


class Account(db.Entity):
    _table_ = 'accounts'
    id = PrimaryKey(int, auto=True)
    item_accounts = Set('ItemAccount')
    name = Required(str)
    number = Optional(str)
    branch = Optional(str)


class User(db.Entity):
    _table_ = 'users'
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    email = Required(str)
    password = Required(str)
    budgets = Set(Budget)


class Item(db.Entity):
    _table_ = 'items'
    id = PrimaryKey(int, auto=True)
    description = Required(str)
    category = Required(Category)
    item_accounts = Set('ItemAccount')
    bucket = Required(Bucket)
    type = Required(str)  # income or expense
    frequency = Required(str)  # weekly, fortnightly, monthly, bimonthly, quarterly, annually
    budget_items = Set('BudgetItem')


class ItemAccount(db.Entity):
    _table_ = 'item_accounts'
    items = Required(Item)
    accounts = Required(Account)
    ratio = Required(float)
    PrimaryKey(items, accounts)


class BudgetItem(db.Entity):
    _table_ = 'budget_items'
    items = Required(Item)
    budgets = Required(Budget)
    amount = Required(float)
    PrimaryKey(items, budgets)


set_sql_debug(True)