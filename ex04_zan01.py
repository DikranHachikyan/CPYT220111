# %%
s1 = 'Lorem ipsum dolor sit amet'
s2 = "Lorem ipsum dolor sit amet"
# %%
s3 = '''Lorem ipsum dolor sit amet,
consectetur adipisicing elit,
sed do eiusmod'''

print(s3)
# %%
def foo():
    '''Function foo()
    prints Hello Foo in terminal
    created: 11.01.2022
    author:me'''
    print('Hello Foo!')


foo()
# %%
print(foo.__doc__)
# %%
x = 12

print(f'value of x ** 2 is {x ** 2}')
# %%
s1[4]
# %%
s1[0:5]
# %%
s1[0:20:2]
# %%
s1[::-1]
# %%
'HELLO'.lower()