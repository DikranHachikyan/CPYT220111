

from draw import Rectangle, Point, ShapeUtils



if __name__ == '__main__':

    pn1 = Point(x = 9, y = 8)
    pn2 = Point(x = 6, y = 4)

    print(f'distance btw {pn1} and {pn2} is {ShapeUtils.distance(pn1, pn2)}')

    rc1 = Rectangle()
    rc2 = Rectangle(x=10, y = 20, w=100, h=20)

    print(f'distance btw rc1 and rc2 is {ShapeUtils.distance(rc1, rc2):.3f}')

    print('---')