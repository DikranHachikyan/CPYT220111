# 1. дефиниция на класа

class Point():
    
    def __init__(self):
        print('Point Ctor')
        # данни на обекта
        self.x = 10
        self.y = 20

    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.x},{self.y})')


if __name__ == '__main__':
    # 2. променлива от тип Point (създаваме обект от тип Point)
    # клас - типът (Point), обект - представители на класа (променливите)
    p1 = Point()

    p1.draw()
    
    p1.x = 12
    p1.y = 15

    p1.draw()

    print('---')