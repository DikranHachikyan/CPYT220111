
if __name__ == '__main__':
#   
    sq = [ x ** 2 for x in range(11)] 
    
    print(f'values={sq}')

    txt = 'Lorem ipsum dolor sit amet'

    letters = [ f'[{t}]' for t in txt]

    print(f'letters:{letters}')


    # for i in range(3):
    #     for j in range(6):
    #         print(f'i={i},j={j}')

    values = [  f'i={i},j={j}' for i in range(5) for j in range(6)]
    print(f'{values}')
    print('---')