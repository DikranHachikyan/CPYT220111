# 1. дефиниция на класа

class Point():
    
    def __init__(self, *args, x=0, y=0, **kwargs):
        print('Point Ctor')
        # данни на обекта
        self.x = x
        self.y = y

    # методи на обекта
    def draw(self):
        print(f'draw point at ({self.x},{self.y})')

    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy

if __name__ == '__main__':
    # 2. променлива от тип Point (създаваме обект от тип Point)
    # клас - типът (Point), обект - представители на класа (променливите)
    p1 = Point()
    p2 = Point(x=40, y=50)

    p1.draw()
    
    p1.x = 12
    p1.y = 15

    p1.draw()
    p2.draw()

    p1.move_to(5,-8)
    p1.draw()
    print('---')