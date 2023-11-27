#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        """initializing the rectangle
        Args:
        width (int): width of the rectangle
        height (int): height of the rectengle
        """
        self.width = width
        self.height= height

    @property
    def width(self):
        """get/set the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = width = width

    @property
    def height(self):
        """get/set the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value
