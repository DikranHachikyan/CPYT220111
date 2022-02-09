# 1
import draw.point as dp

if __name__ == '__main__':

    print(f'count:{dp.Point.count}')

    p1 = dp.Point(x=10, y=20)
    p2 = dp.Point(x=30, y=30)

    p1.draw()
    
    del p1
    p2.draw()
    print('---')