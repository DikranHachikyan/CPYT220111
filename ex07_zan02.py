# %%
conn = dict(
    db='northwind',
    port=1521,
    encoding='utf8',
    host='localhost',
    keepalive=True
)

print(conn['db'])
# %%
conn1 = ['localhost',1521,'utf8','northwind', True]

print(conn1[1])
# %%
user = {
    'firstname':'Anna',
    'lastname':'Smith',
    'age':30,
    'mail':'anna@no.com'
}


type(user) is dict
# %%
user.keys()
# %%
user.values()
# %%
user.items()
# %%
'age' in user
# %%
user['phone']
# %%
user.get('phone', '000-00-00')
# %%
