# глобална променлива
port = 3306
# 1. дефиниция на функцията
def show():
    port = 22
    print(f'show port:{port}')


if __name__ == '__main__':
#   
    # 2. извикване на функ.
    print(f'before:{port}')
    show()
    print(f'after:{port}')
    print('---')