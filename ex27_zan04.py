# глобална променлива
service = 'ssh'
# 1. дефиниция на функцията
def sum_numbers(a,b):
    # тяло на функцията
    # c - локална променлива
    c = a + b
    return c


if __name__ == '__main__':
#   
    # 2. извикване на функ.
    sm1 = sum_numbers(5,6)

    x,y = 12,11

    sm2 = sum_numbers(x,y)
    
    print(f'sm1 = {sm1} sm2 = {sm2}')
    print('---')