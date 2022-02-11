
from math import sqrt
from draw import Rectangle, Point


class ShapeUtils():


    # стат. метод може да работи само със статични данни  и методи на класа
    @staticmethod
    def distance(p1,p2):
        if not isinstance(p1, Point) or not isinstance(p2, Point):
            raise TypeError('Parameters must be instances of Point')
        
        dx = (p1.x - p2.x) ** 2
        dy = (p1.y - p2.y) ** 2
    
        return sqrt(dx + dy)

    def foo(self):
        print('Method Foo')

if __name__ == '__main__':

    pn1 = Point(x = 9, y = 8)
    pn2 = Point(x = 6, y = 4)

    print(f'distance btw {pn1} and {pn2} is {ShapeUtils.distance(pn1, pn2)}')

    rc1 = Rectangle()
    rc2 = Rectangle(x=10, y = 20, w=100, h=20)

    print(f'distance btw rc1 and rc2 is {ShapeUtils.distance(rc1, rc2):.3f}')

    print('---')