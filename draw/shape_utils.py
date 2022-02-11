
from math import sqrt
from draw import Point

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