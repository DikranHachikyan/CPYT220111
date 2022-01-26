# глобална променлива

# 1. дефиниция на функцията
def show(title, *args, a=100, **kwargs):
    print(f'title={title}')

    print(f'args:')
    for v in args:
        print(v, end=' ')
    print()

    print(f'keyword-only args:{a}')

    print('kwargs:')
    kw = {
        'p':kwargs.get('path','/tmp'),
        'v':kwargs.get('version','0.1')
    }
    print(f'kwargs:{kw}')


if __name__ == '__main__':
#   
    # 2. извикване на функ.
    


    app = {
        'service':'mysql',
        'path':'/usr/local', 
        'port':3307,
        'version':'1.2.3'
    }
    show('Title', 5,2,4, **app)
    show('Title', 5,2,4,a = 22, **app)
    print('---')