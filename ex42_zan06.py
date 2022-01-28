# глобална променлива

# 1. дефиниция на функцията
# 100 + 99 + 98 + .... + 1 = 5050
def get_squares(n):
    return [ v ** 2 for v in range(1, n + 1)]

# 1. дефиниция
def generate_squares(n):
    for v in range(1, n + 1):
        yield v ** 2 


if __name__ == '__main__':
#   
    values = get_squares(10)
    print(f'values:{values}')

    # 2. присвояваме на променлива
    gs = generate_squares(10)

    print(type(generate_squares))
    print(type(gs))

    print(f'1 => {next(gs)}')
    print(f'2 => {next(gs)}')
    print(f'3 => {next(gs)}')
    print(f'4 => {next(gs)}')

    arr = list(gs)
    print(f'arr:{arr}')
    # exception StopIteration    
    # print(f'11 => {next(gs)}')

    gs2 = generate_squares(5)

    for v in gs2:
        print(f'v={v}')

    print('---')