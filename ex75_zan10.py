
from draw import Rectangle, Point


if __name__ == '__main__':

    rc1 = Rectangle(x = 15, y = 30, w = 150, h = 190)
    rc2 = Rectangle(x = 10, y = 20, w = 120, h = 160)

    if rc1 > rc2:
        print(f'{rc1} > {rc2}')

    print('---')