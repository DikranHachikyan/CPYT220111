from functools import wraps


def to_uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.__original = func
        args = [ f'{v}'.upper() for v in args]
        return func(*args, **kwargs)
    return wrapper



if __name__ == '__main__':

    print('Hello ', 'Python', 'lorem', 'ipsum')

    print = to_uppercase(print)
    print('Hello ', 'Python', 'lorem', 'ipsum')
    print(11,22, 'a', 12)

    print = print.__original
    print('Hello ', 'Python', 'lorem', 'ipsum')

    print('---')