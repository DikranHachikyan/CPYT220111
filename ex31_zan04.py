# глобална променлива

# 1. дефиниция на функцията
def show(title,a=100, *args, **kwargs):
    print(f'title={title}')

    print(f'optional param a:{a}')

    print(f'args:')
    for v in args:
        print(v, end=' ')
    print()

    print('kwargs:')
    kw = {
        'p':kwargs.get('path','/tmp'),
        'v':kwargs.get('version','0.1')
    }
    print(f'kwargs:{kw}')


if __name__ == '__main__':
#   
    # 2. извикване на функ.
    # show('Text Editor')

    # show('Text Editor', 12)

    # show('Text Editor', 12, 1,2,3,4)

    show('Text Editor', 12, 1,2,3,4, path='/usr/local', version='1.2.3')
    show('Text Editor', 12, 1,2,3,4, version='3.2.3',path='/usr/lib')
    show('Text Editor', 12, 1,2,3,4, version='3.3.3')
    app = {
        'service':'mysql',
        'path':'/usr/local', 
        'port':3307,
        'version':'1.2.3'
    }
    show('Title', 11, 2,3,4,5, **app)
    print('---')