def print_key(key, **kwargs):
    try:
        print(f'{key} =>{kwargs[key]}')
    except KeyError as e:
        # 3. добро решение
        raise
        # 2. (не е добро решение)
        # pass

        # 1. вариант (не е добро решение)
        # print(f'Invalid key:{e}')


if __name__ == '__main__':

    conn = {
        'host':'localhost',
        'port':1521,
        'service':'oracle'
    }
    try:
        print_key('host', **conn)
        print_key('ip', **conn)
    except KeyError as e:
        # pass
        print(f'Invalid key:{e}')

    print('---')