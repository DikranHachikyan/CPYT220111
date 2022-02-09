# 1. дефиниция на класа

class A():
    pass

class Point():
    
    def __init__(self, *args, x=0, y=0, **kwargs):
        print('Point Ctor')
        # данни на обекта
        self.x = x
        self.y = y
        self.is_visible = True

    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.x},{self.y})')

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
        assert type(x) is int and x >=0, f'x must be positive int number ({x})' 
        self.__x = x

    @property    
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        assert type(y) is int and y >=0, f'y must be positive int number ({y})' 
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

if __name__ == '__main__':
    # 2. променлива от тип Point (създаваме обект от тип Point)
    # клас - типът (Point), обект - представители на класа (променливите)
    p1 = Point(x=40, y=50)
    p2 = Point(x=14, y=15)
    # a = A()
    print(f'Point object:{p1}')
    # p = p1
    if p1 == p2:
        print(f'{p1} equals {p2}')
    else:
        print(f'{p1} does not equal {p2}')

    # if p1 == a:
    #     print('test')
    print('---')