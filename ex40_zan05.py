# глобална променлива

# 1. дефиниция на функцията
# 100 + 99 + 98 + .... + 1 = 5050



if __name__ == '__main__':
#   
    numbers = [3,5,2,1,8]
    # 2. извикване на функ.
    pow_xy = lambda x,y: x ** y

    z = pow_xy(2,4)
    print(f'z={z}')

    for v in map(lambda e: e * 2 , numbers):
        print(v)
        
    print('---')