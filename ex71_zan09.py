# 1. дефиниция на класа

from math import sqrt


class Point():
    # данни на класа (статични)
    count = 0
    def __init__(self, *args, x=0, y=0, **kwargs):
        print('Point Ctor')
        # данни на обекта
        self.x = x
        self.y = y
        self.is_visible = True
        Point.count +=1

    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.x},{self.y}) n:{Point.count}')

    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy  

    # методи за достъп до данните
    @property
    def x(self):
        # !! така се получава рекурсия!!
        # return self.x
        return self.__x

    @x.setter
    def x(self, x):
        # if x < 0:
        #     raise ValueError(f'negative value:{x}') 
        assert isinstance(x,(int,float)) and x >=0, f'x must be positive int number ({x})' 
        self.__x = x

    @property    
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        assert isinstance(y, (int,float)) and y >=0, f'y must be positive int number ({y})' 
        self.__y = y

    @property
    def is_visible(self):
        return self.__visible
    
    @is_visible.setter
    def is_visible(self, v):
        assert type(v) is bool, f'visible must be boolean value ({v})' 
        self.__visible = v

    # специални методи
    # предефиниране на метод (function override)
    def __str__(self):
        return f'({self.x},{self.y}:visible {self.is_visible})'

    def __eq__(self, other):
        # self - ляв операнд
        # other - десен операнд
        if not isinstance(other, Point):
            raise NotImplementedError(f'Not yet implemented')
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        if not isinstance(other, Point):
            raise NotImplementedError(f'Not yet implemented')
        
        dx1 = self.x ** 2
        dy1 = self.y ** 2
        dist1 = sqrt(dx1 + dy1)

        dx2 = other.x ** 2
        dy2 = other.y ** 2
        dist2 = sqrt(dx2 + dy2)

        return dist1 > dist2

    def __add__(self,other):
        if isinstance(other,Point):
            new_x = self.x + other.x
            new_y = self.y + other.y
        elif isinstance(other, (int,float)):
            new_x = self.x + other
            new_y = self.y + other
        else:
            raise NotImplementedError(f'Not yet implemented')

        return Point(x=new_x, y=new_y)
    
    # унищожаване на обекти

    def __del__(self):
        Point.count -=1
        print(f'Object {self.x},{self.y} destroyed! n:{Point.count}')


def show():
    # p - локална променлива
    p = Point()
    print(f'show:{p} n:{Point.count}')

if __name__ == '__main__':
    # 2. променлива от тип Point (създаваме обект от тип Point)
    # клас - типът (Point), обект - представители на класа (променливите)
    print(f'count:{Point.count}')

    p1 = Point(x=10, y=20)
    p2 = Point(x=30, y=30)

    p1.draw()
    show()
    del p1
    p2.draw()
    print('---')