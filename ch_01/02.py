from sqlalchemy import MetaData
metadata = MetaData()

from sqlalchemy import Table, Column, Integer, Numeric, String

from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')


cookies = Table('cookies', metadata,
    Column('cookie_id', Integer(), primary_key=True),
    Column('cookie_name', String(50), index=True),
    Column('cookie_recipe_url', String(50)),
    Column('cookie_sku', String(50)),
    Column('quantity', Integer()),
    Column('unit_cost', Numeric(12, 2))
)


from datetime import datetime
from sqlalchemy import DateTime

users = Table('users', metadata,
    Column('user_id', Integer(), primary_key=True),
    Column('username', String(15), nullable=False, unique=True),
    Column('email_address', String(255), nullable=False),
    Column('phone', String(20), nullable=False),
    Column('passowrd', String(25), nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)

)


from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint

PrimaryKeyConstraint('user_id', name='user_pk')

UniqueConstraint('username', name='uix_username')

CheckConstraint('unit_cost >= 0.00', name='unit_cost_positive')


from sqlalchemy import Index

Index('ix_cookies_cookie_name', 'cookie_name')


from sqlalchemy import ForeignKey, Boolean
orders = Table('orders', metadata,
    Column('order_id', Integer(), primary_key=True),
    Column('user_id', ForeignKey('users.user_id')),
    Column('shipped', Boolean(), default=False)
)

line_items = Table('line_items', metadata,
    Column('line_items_id', Integer(), primary_key=True),
    Column('order_id', ForeignKey('orders.order_id')),
    Column('cookie_id', ForeignKey('cookies.cookie_id')),
    Column('quantity', Integer()),
    Column('extended_cost', Numeric(12, 2))
)
