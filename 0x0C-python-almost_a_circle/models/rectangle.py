#!/usr/bin/python3
"""rectangles home base"""
from models.base import Base
class Rectangle(Base):
    """the rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """making rectangle"""
        super().__init__(id)
        self.height=height
        self.width=width
        self.x=x
        self.y=y

    def area(self):
        """area"""
        return self.height * self.width

    def display(self):
        for row in range(self.y):
            print()
        for row in range(self.height):
            for column in range(self.x):
                print(" ", end="")
            for column in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """update"""
        numbarg=0
        if args:
            for arg in args:
                numbarg+=1
                if numbarg == 1:
                    self.id = arg
                if numbarg == 2:
                    self.width = arg
                if numbarg == 3:
                    self.height = arg
                if numbarg == 4:
                    self.x = arg
                if numbarg == 5:
                    self.y = arg
        elif kwargs:
            for arg in kwargs.keys():
                if arg == "id":
                    self.id = kwargs.get(arg)
                if arg == "width":
                    self.width = kwargs.get(arg)
                if arg == "height":
                    self.height = kwargs.get(arg)
                if arg == "x":
                    self.x = kwargs.get(arg)
                if arg == "y":
                    self.y =kwargs.get(arg)
    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, height):
        """height"""
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height=height

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, width):
        """width"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width=width

    @property
    def x(self):
        """x"""
        return self.__x

    @x.setter
    def x(self, x):
        """x"""
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x=x

    @property
    def y(self):
        """y"""
        return self.__y

    @y.setter
    def y(self, y):
        """y"""
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y=y

    def __str__(self):
        """stringle"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)
