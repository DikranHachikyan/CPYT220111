# глобална променлива
service = 'ssh'
# 1. дефиниция на функцията
def sum_numbers(a, b, *args):
    # тяло на функцията
    # c - локална променлива
    c = a + b
    print(f'args:{args}')
    for v in args:
        c += v
    return c


if __name__ == '__main__':
#   
    # 2. извикване на функ.
    sm1 = sum_numbers(5,6)

    x,y,z, m, n, t = 12,11,4,6,8,9

    sm2 = sum_numbers(x,y,z,m,n,t)
    
    values = [i for i in range(3,10)]

    sm3 = sum_numbers(x,y, *values)

    print(f'sm1 = {sm1} sm2 = {sm2} sm3={sm3}')
    print('---')