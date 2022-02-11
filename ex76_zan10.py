
from draw import Rectangle, Point


if __name__ == '__main__':

    shapes = [ Rectangle(x=1,y=2, w=10,h=20), Point(), Point(x=20,y=40), Rectangle(x=11,y=22, w=40,h=50)]

    for s in shapes:
        s.draw()
        s.move_to(10,20)
        s.draw()
        
    print('---')