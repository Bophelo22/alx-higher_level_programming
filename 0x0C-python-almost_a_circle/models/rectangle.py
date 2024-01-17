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
        return (self.width * self.height)
        
    
    def display(self):
        """public method that prints in stdout the
        Rectangle instance with the character"""
        for col in range(self.y):
            print()
        for y in range(self.height):
            for x in range(self.x):
                print(' ', end='')
            for row in range(self.width):
                print('#', end='')
            print()
            
    def __str__(self):
        """overriding the __str__ method"""
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.x, self.y, self.width, self.height))
        
    def update(self, *args, **kwargs):
        """function that assigns a key/value argument to attributes"""
        argument_counter = len(args)
        if argument_counter > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
    
    def to_dictionary(self):
        """public method that returns the dictionary representation of a Rectangle"""
        
        return {'x': self.x, 'y': self.y,'id': self.id,
               'height': self.height, 'width': self.width}
