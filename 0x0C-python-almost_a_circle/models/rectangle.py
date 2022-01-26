#!/usr/bin/python3
"""rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle importation"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The wide"""
        return self.__width

    @property
    def height(self):
        """The tall"""
        return self.__height

    @property
    def x(self):
        """The x"""
        return self.__x

    @property
    def y(self):
        """The y"""
        return self.__y

    @width.setter
    def width(self, value):
        """the wides"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """the talls"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """the xs"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        """the wise"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """the area of the squarea"""
        return self.height * self.width

    def display(self):
        """displays the shape"""
        for row in range(self.y):
            print("")
        for row in range(self.height):
            for column in range(self.x):
                print(" ", end="")
            for column in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """overridden str method"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """changes values of variables"""
        id = ["id", "width", "height", "x", "y"]
        g = 0
        if args:
            for arg in args:
                setattr(self, id[g], args[g])
                g += 1
        elif kwargs:
            for arg in kwargs:
                setattr(self, arg, kwargs[arg])
