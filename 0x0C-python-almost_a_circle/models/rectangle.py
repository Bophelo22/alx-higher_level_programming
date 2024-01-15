#!/usr/bin/python3
"""Class Rectangle inherits from Base"""
from models.base import Base
class Rectangle(Base):
    """Private instance attributes, each with its own public getter and setter"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """public getter for width"""
        return self.__width
    
    @width.setter
    def width(self, val):
        """public setter for width"""
        if type(val) != int:
            return TypeError("width must be an int")
        elif val < 0:
            return TypeError("width must be > 0")
        else:
            self.__width = val
    
    @property 
    def height(self):
        """public getter for height"""
        return self.__height
    
    @height.setter
    def height(self,val):
        """public setter for height"""
        
        if val != int:
            return TypeError("height must be an int")
        elif val < 0:
            return TypeError("height must be > 0")
        else: 
            self.__height = val
    
    @property 
    def x(self):
        """public setter for x"""
        return self.__x
    
    @x.setter
    def x(self,val):
        """publis setter for x"""
        if val != int:
           return TypeError("x must be an int")
        elif val < 0: 
            return TypeError("x must be >= 0")
        else:
            self.__x = val
    
    @property 
    def y(self):
        """public setter for y"""
        return self.__y
    
    @x.setter
    def y(self,val):
        """publis setter for y"""
        if val != int:
           return TypeError("y must be an int")
        elif val < 0: 
            return TypeError("y must must be >= 0")
        else:
            self.__y = val
            
    
    def area(self):
        """function that determines the area"""
        area = self.__width * self.__height
        return (area)
    
    def display(self):
        """public method that prints in stdout the
        Rectangle instance with the character"""
        print_symb = "#"
        rect = ""
        
        for i in range(self.height):
            rect += (" " * self.x) + (print_symb*self.width) + "\n"
        print(rect, end="")
            
    def __str__(self):
        """overriding the __str__ method"""
        return f"[{type(self).__name__}] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
    
    def display(self):
        """public method to print in stdout the Rectangle instance with the character"""
        
    def update(self, *args, **kwargs):
        """function that assigns a key/value argument to attributes"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass
    
    def to_dictionary(self):
        """public method that returns the dictionary representation of a Rectangle"""
        
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),'id': getattr(self, "id"),
               'height': getattr(self, "height"), 'width': getattr(self, "width")}
