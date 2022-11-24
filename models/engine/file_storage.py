#!/usr/bin/python3
"""
This module contains the FileStorage class that serializes instances to a JSON\
 file and deserializes JSON file to instances

Private instance attributes:
    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary - empty but will store all objects by <class name>.\
    id (ex: to store a BaseModel object with id=12121212,\
    the key will be BaseModel.12121212)

Public instance methods:
    all(self): returns the dictionary __objects
    new(self, obj): sets in __objects the obj with key <obj class name>.id
    save(self): serializes __objects to the JSON file (path: __file_path)
    reload(self): deserializes the JSON file to __objects \
    only if the JSON file (__file_path) exists ; otherwise, do nothing.\
    If the file doesn't exist, no exception should be raised)
"""
import json


class FileStorage:
    """ This is the base class of the models. It contains the core features\
    that will be inherited by all forms of models in the application """
    __file_path = "storage.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        pass

    def save(self):
        with open(type(self).__file_path, "w") as f:
            json.dump(type(self).__objects, f)

    def reload(self):
        if path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                type(self).__objects = json.loads(f.read())
