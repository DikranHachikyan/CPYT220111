from draw import Point

class Rectangle(Point):

    def __init__(self,*args, x=0, y=0, w=0, h=0, **kwargs):
        # извикване на инит. метода на родителя
        super().__init__(*args, x=x, y=y, **kwargs)
        print('Rectangle Ctor')
        self.width = w
        self.height = h

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        assert isinstance(w, (float,int)) and w >= 0, 'width must be positive number'
        self.__width = w
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,h):
        assert isinstance(h, (float,int)) and h >= 0, 'height must be positive number'
        self.__height = h

    # Override
    def draw(self):
        super().draw()
        print(f'rectangle:[{self.width}, {self.height}]')

    def __str__(self):
        point_str = super().__str__()
        return f'{point_str}[{self.width} x {self.height}]'

    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            raise NotImplementedError(f'Not yet implemented')   
        p = super().__gt__(other)

        return p and (self.width * self.height) > (other.width * other.height) 