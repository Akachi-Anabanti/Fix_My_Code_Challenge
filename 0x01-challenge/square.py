#!/usr/bin/python3
"""A module that defines a square class"""


class square:
    """Defines a square class"""
    __width = 0
    __height = 0

    def __init__(self, *args, **kwargs):
        if ("width" not in kwargs.keys() or "height"
                not in kwargs.keys()):
            raise AttributeError("Please provide both height and width")
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        """width setter method"""
        if type(value) != int:
            raise TypeError("width is not a valid type")
        if (value <= 0):
            raise ValueError("width cannot be <= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter method"""
        if type(value) != int:
            raise TypeError("height is not a valid type")
        if value <= 0:
            raise ValueError("height cannot be <= 0")
        self.__height = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """calculates area perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """string method"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
