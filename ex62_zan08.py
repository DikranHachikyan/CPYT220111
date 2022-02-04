# 1. дефиниция на класа

class Point():
    
    def __init__(self, *args, x=0, y=0, **kwargs):
        print('Point Ctor')
        # данни на обекта
        self.__x = x
        self.y = y

    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.__x},{self.y})')

    def move_to(self, dx, dy):
        self.__x += dx
        self.y += dy

if __name__ == '__main__':
    # 2. променлива от тип Point (създаваме обект от тип Point)
    # клас - типът (Point), обект - представители на класа (променливите)
    p1 = Point(x=40, y=50)

    # ! Внимание
    # p1.__x = -10
    # print(f'x of p1 is {p1.__x}')

    p1.draw()
    print('---')