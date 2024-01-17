#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """objects of the class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Square class inherits from Rectangle"""
        super().__init__(size, size, x, y, id)
        self.size = size
    
    @property
    def size(self):
        """public getter for size"""
        return self.width

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
    
    def __str__(self):
        '''
        String representation
        '''
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y, self.size)
        
    def update(self, *args, **kwargs):
        """ public method that assigns attributes"""
        argument_counter = len(args)
        if argument_counter > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except BaseException:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
        
    def to_dictionary(self):
        """public method that returns the dictionary representation of a Square"""
        
        return {'id': self.id, 'x': self.x, 
                'size': self.size,'y': self.y}
