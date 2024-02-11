#!/usr/bin/python3
"""
AirBnB clone File storage
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file and deserializes
    JSON file to instances

    """

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        sets in __objects the obj with
        key <obj class name>.id
        """

        obj_class_name = obj.__class__.__name__
        key = f"{obj_class_name}.{obj.id}"
        FileStorge.__objects[key] = obj

    def all(self):
        """
        returns the dictionary __objects
        """

        return FileStorage.__objects

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """

        all_objs = FileStorge.__objects
        obj_dict = {}
        for key, obj in all_obj.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dumb(obj_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.isfile(FileStorge.__file_path):
            with open(FileStorge.__file_path, "r", encoding="utf-8"):
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.item():
                        obj = self.class_dict[value['__class__']](**value)
                        self.__objects[key] = obj
                except Exception:
                    pass
