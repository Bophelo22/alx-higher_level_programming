#!/usr/bin/python3
"""Defines a base model class."""
import json
class Base:
    """Represent the base model.

    Represents the "base" for all other classes in project 0x0C*."""
    __nb_objects = 0
    def __init__(self, id=None):
        """Initialize a new Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """ method that returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
        
    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes the JSON string representation of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dic = [o.to_dictionary() for o in list_objs]
                json_file.write(Base.to_json_string(list_dic))
                
    @staticmethod
    def from_json_string(json_string):
        """static method that returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)
        
    @classmethod
    def create(cls, **dictionary):
        """class method that returns an instance with all attributes already set:"""
        if dictionary != {}:
            if cls.__name__ is "Rectangle":
                new_instance = cls(1,1)
            else:
                new_instance = cls(1)
            new_instance.update(**dictionary)
            return new_instance
    
    @classmethod
    def load_from_file(cls):
        """class method that returns a list of instances:"""
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name,"r") as json_file:
                list_dic = Base.from_json_string(json_file.read())
                return [cls.create(**dic) for dic in list_dic]
        except IOError:
            return []
