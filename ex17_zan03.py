
if __name__ == '__main__':
#   2 + 4 + ... + 98 + 100 = 2550 

    i = 1
    suma = 0

    while i <= 100:
        i += 1
        
        if i == 10: 
            break
        
        suma += i
    else:
        print('--- else ---')

    print(f'2 + 4 + ... + 98 + 100 = {suma}')
    print('---')