# глобална променлива

# 1. дефиниция на функцията


def foo(a=None, b=None):
    if not a: a = []
    if not b: b = {}
    
    print(f'a={a}')
    print(f'b={b}')
    print('-' * 30)
    n = len(a)
    a.append(n)
    b[n] = n

if __name__ == '__main__':
#   
    # 2. извикване на функ.
    foo()
    foo([4,5,6], {'z':10})
    foo()
    foo([14,51,26], {'z':10, 'x':20})
    foo()
    print('---')