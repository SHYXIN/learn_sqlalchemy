from get_engine import engine, cookies

# 导入engine
connection = engine.connect()
print(connection)

# Example 2-1 Single insert as a method
ins = cookies.insert().values(
    cookie_name='chocolate chip',
    cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
    cookie_sku='CC01',
    quantity="12",
    unit_cost="0.05"
)
# 查看语句
print(str(ins))
# INSERT INTO cookies (cookie_name, cookie_recipe_url, cookie_sku, quantity, unit_cost)
# VALUES (:cookie_name, :cookie_recipe_url, :cookie_sku, :quantity, :unit_cost)

# 查看参数
print(ins.compile().params)
# {'cookie_recipe_url': 'http://some.aweso.me/cookie/recipe.html', 'unit_cost': '0.05',
# 'cookie_sku': 'CC01', 'quantity': '12', 'cookie_name': 'chocolate chip'}

result = connection.execute(ins)

print(result.inserted_primary_key)
# [1]

from sqlalchemy import insert
ins = insert(cookies).values(
    cookie_name="chocolate chip",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50"
)
print(str(ins))

ins = cookies.insert()
result = connection.execute(ins, cookie_name='dark chocolate chip',
                            cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
                            cookie_sku='CC02',
                            quantity='1',
                            unit_cost='0.75'
                            )
print(result.inserted_primary_key)

inventory_list = [
    {
        'cookie_name': 'penaut butter',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
        'cookie_sku': 'PB01',
        'quantity': '24',
        'unit_cost': '0.25'
    },
    {
        'cookie_name':'oatmeal raisin',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
        'cookie_sku': '100',
        'quantity': '100',
        'unit_cost': '1.00'

    }
]

result = connection.execute(ins, inventory_list)


# Query data
print('Query_data')

from sqlalchemy import select

s = select([cookies])

print(str(s))

rp = connection.execute(s)
results = rp.fetchall()
print(results)
first_row = results[0]
print(first_row[0])
print(first_row.cookie_name)
print(cookies.c)
print(first_row[cookies.c.cookie_name])

rp = connection.execute(s)
for record in rp:
    print(record.cookie_name)

s = select([cookies.c.cookie_name, cookies.c.quantity])
rp = connection.execute(s)
print(rp.keys())
result = rp.first()
print(result)

# Order
s = select([cookies.c.cookie_name, cookies.c.quantity])
s = s.order_by(cookies.c.quantity)
rp = connection.execute(s)
for cookie in rp:
    print('{} -  {}'.format(cookie.quantity, cookie.cookie_name))

# desc
from sqlalchemy import desc, asc
s = select([cookies.c.cookie_name, cookies.c.quantity])
s = s.order_by(desc(cookies.c.quantity))
rp = connection.execute(s)
for cookie in rp:
    print('{} -  {}'.format(cookie.quantity, cookie.cookie_name))

s = select([cookies.c.cookie_name, cookies.c.quantity])
s = s.order_by(cookies.c.quantity)
s = s.limit(2)
rp = connection.execute(s)
print([result.cookie_name for result in rp])


from sqlalchemy.sql import func
s = select([func.sum(cookies.c.quantity)])
rp = connection.execute(s)
print(rp.scalar())

s = select([func.count(cookies.c.cookie_name)])
rp = connection.execute(s)
record = rp.first()
print(record)
print(record.keys())
print(record.count_1)

# Example 2-16. Renaming our count column
s = select([func.count(cookies.c.cookie_name).label('inventory_count')])
rp = connection.execute(s)
record = rp.first()
print(record.keys())
print(record.inventory_count)


# Filter
s = select([cookies]).where(cookies.c.cookie_name == 'chocolate chip')
print(str(s))
rp = connection.execute(s)
record = rp.first()
print(record.items())

# like
s = select([cookies]).where(cookies.c.cookie_name.like('%chocolate%'))
rp = connection.execute(s)
print(str(s))
for record in rp.fetchall():
    print(record.cookie_name)


# Operators
s = select([cookies.c.cookie_name, 'SKU-' + cookies.c.cookie_sku])
for row in connection.execute(s):
    print(row)
# ('chocolate chip', 'SKU-CC01')
# ('dark chocolate chip', 'SKU-CC02')
# ('penaut butter', 'SKU-PB01')
# ('oatmeal raisin', 'SKU-100')


from sqlalchemy import cast, Numeric
s = select([cookies.c.cookie_name,
            cast((cookies.c.quantity * cookies.c.unit_cost), Numeric(12, 2)).label('inv_cost')])
for row in connection.execute(s):
    print("{} -  {}".format(row.cookie_name, row.inv_cost))

