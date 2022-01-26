# глобална променлива

# 1. дефиниция на функцията
# 100 + 99 + 98 + .... + 1 = 5050

def sum_n(n):
    print(f'n={n}')
    if n > 0:
        return n + sum_n(n - 1)
    return 0

if __name__ == '__main__':
#   
    # 2. извикване на функ.
    result = sum_n(5)
    print(f'result = {result}')
    print('---')