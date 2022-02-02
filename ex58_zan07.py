class NameNotFoundError(Exception):
    pass

def print_key(key, **kwargs):
    try:
        print(f'{key} =>{kwargs[key]}')
    except KeyError:
        raise NameNotFoundError('Please, check ... ')
        
    

if __name__ == '__main__':

    conn = {
        'host':'localhost',
        'port':1521,
        'service':'oracle'
    }
    try:
        print_key('host', **conn)
        print_key('ip', **conn)
    except NameNotFoundError as e:
        # pass
        print(f'Invalid key:{e}')

    print('---')