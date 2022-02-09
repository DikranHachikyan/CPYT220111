# 1
# from draw.point import Point

# 2
# import draw.Point as Point
from draw import Point

if __name__ == '__main__':

    print(f'count:{Point.count}')

    p1 = Point(x=10, y=20)
    p2 = Point(x=30, y=30)

    p1.draw()
    
    del p1
    p2.draw()
    print('---')