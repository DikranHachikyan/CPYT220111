# 1
# import time
# print(time.time())

# 1.1
# import time as tm
# print(tm.time())

# 2
# from time import time,sleep
# print(time())

# 2.1
# from time import time as get_time
# print(get_time())
from time import time, sleep
from functools import wraps

def measure(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        t = time()
        func(*args,**kwargs)
        print(f'{func.__name__}:{time() - t:.4f}')
    return wrapper


@measure
def foo(sleep_time=0.3):
    '''Function foo sleeps sleep_time seconds'''
    sleep(sleep_time)



if __name__ == '__main__':

    foo()
    foo(0.5)
    print(f'{foo.__name__}, doc str:{foo.__doc__}')
    print('---')