# глобална променлива


if __name__ == '__main__':

    squares = ( v ** 2 for v in range(5, 50, 5))

    print(f'1=>{next(squares)}')
    print(f'2=>{next(squares)}')
    print(f'3=>{next(squares)}')
    print(f'4=>{next(squares)}')
    print(f'5=>{next(squares)}')

    print('---')