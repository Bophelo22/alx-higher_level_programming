#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
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
        return json.dumps(list_dictionaries)
        
    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes the JSON string representation of list_objs to a file"""
        list_dic = []
        if not list_objs:
            list_objs = []
        for i in list_objs:
            list_dic.append(i.to_dictionary())

        with open('{}.json'.format(cls.__name__), 'w', encoding='utf-8') as json_file:
            json_file.write(cls.to_json_string(list_dic))
                
    @staticmethod
    def from_json_string(json_string):
        """static method that returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)
        
    @classmethod
    def create(cls, **dictionary):
        """class method that returns an instance with all attributes already set:"""
        if cls.__name__ is 'Rectangle':
            newInstance = cls(1, 1)
            newInstance.update(**dictionary)
            return newInstance
        if cls.__name__ is 'Square':
            newInstance = cls(1)
            newInstance.update(**dictionary)
            return newInstance
        else:
            return None
    
    @classmethod
    def load_from_file(cls):
        """class method that returns a list of instances:"""
        instance_list = []
        try:
            with open('{}.json'.format(cls.__name__), 'r',
                      encoding='utf-8') as json_file:
                objectList = cls.from_json_string(json_file.read())
        except IOError:
            return []
        for dictionary in objectList:
            instance_list.append(cls.create(**dictionary))
        return instance_list
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
        Wrte to csv
        '''
        list_to_dic = []
        if list_objs is not None:
            list_objs = []
        for i in list_objs:
            list_to_dic.append(i.to_dictionary())

        with open('{}.csv'.format(cls.__name__), 'w', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''
        Returns a list
        of instances
        '''
        instance_list = []
        try:
            with open('{}'.format(cls.__name__), 'r', encoding='utf-8') as csv_file:
                obj_list = cls.from_json_string(csv_file.read())
        except IOError:
            return []
        for dic in obj_list:
            instance_list.append(cls.create(**dic))
        return instance_list
