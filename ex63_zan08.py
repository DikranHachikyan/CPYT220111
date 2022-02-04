# 1. дефиниция на класа

class Point():
    
    def __init__(self, *args, x=0, y=0, **kwargs):
        print('Point Ctor')
        # данни на обекта
        self.set_x(x)
        self.set_y(y)
        self.set_visible(True)

    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.get_x()},{self.get_y()})')

    def move_to(self, dx, dy):
        self.set_x( self.get_x() + dx )
        self.set_y( self.get_y() + dy ) 

    # методи за достъп до данните
    def set_x(self, x):
        self.__x = x
    
    def set_y(self, y):
        self.__y = y

    def set_visible(self, v):
        self.__visible = v

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    def is_visible(self):
        return self.__visible

if __name__ == '__main__':
    # 2. променлива от тип Point (създаваме обект от тип Point)
    # клас - типът (Point), обект - представители на класа (променливите)
    p1 = Point(x=40, y=50)


    p1.draw()
    p1.set_y(-10)
    p1.draw()
    p1.move_to(-6, 10)
    p1.draw()
    print('---')