

from draw import Rectangle, Point, ShapeUtils



if __name__ == '__main__':
    p = Point(x=10, y=20)

    p.draw()
    p.move_to(10,20)
    p.draw()

    p2 = Point.from_point(p)
    print(f'p2:{p2}')
    
    print('---')