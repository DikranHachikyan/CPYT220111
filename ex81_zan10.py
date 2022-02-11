
def sum_numbers(a: float, b: float)->float:
    return a + b

if __name__ == '__main__':
    x, y = 5, 6

    s = sum_numbers(x, y)

    print(f's = {s}')
    
    s = sum_numbers('Pyt','hon')

    print(f's = {s}')

    print(sum_numbers.__annotations__)
    
    print('---')