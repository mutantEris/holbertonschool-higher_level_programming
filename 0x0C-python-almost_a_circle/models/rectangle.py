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
        for row in range(self.height):
            for column in range(self.width):
                print("#", end="")
            print()

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
