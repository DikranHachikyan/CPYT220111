# глобална променлива

# 1. дефиниция на функцията
# 100 + 99 + 98 + .... + 1 = 5050

if __name__ == '__main__':
#   
    items = [('A', 5, 7), ('D', 2, 6), ('B', 5, 1), ('D', 2, 5)]

    # 1
    # items.sort()

    # 2.
    # items.sort(key=lambda el: el[1])
    # sorted items:[('D', 2, 6), ('D', 2, 5), ('B', 4, 8), ('A', 5, 7)]
    
    items.sort(key=lambda el: (el[1],el[0],el[2]) )

    print(f'sorted items:{items}')
        
    print('---')