
from draw import Rectangle, ShapeMixin


class CRectangle(Rectangle, ShapeMixin):
    pass

if __name__ == '__main__':

    cr = CRectangle(x = 10, y = 20, w = 100, h=20)

    cr.draw()
    s = cr.get_area()
    print(f'Rectangle area:{s}')
        
    print('---')