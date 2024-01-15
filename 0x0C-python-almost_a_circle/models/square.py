#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """objects of the class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        """public getter for size"""
        return self.__width

    @size.setter
    def size(self, val):
        """public setter for size"""
        if type(val) != int:
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = val
            self.height = val
            
    def update(self, *args, **kwargs):
        """ public method that assigns attributes"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key,val)
            return
        
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass
        
    def to_dictionary(self):
        """public method that returns the dictionary representation of a Square"""
        
        return {'id': getattr(self,"id"), 'x': getattr(self,"x"), 
                'size': getattr(self,"szie"),'y': getattr(self,"y")}
