#!/usr/bin/python3
"""
<<<<<<< HEAD
AirBnB clone File storage
"""

import json
=======
module
"""

import json
import os
>>>>>>> 281e15e5d5aa3ae94c715583453a3205c97157ff
from models.base_model import BaseModel


class FileStorage:
    """
<<<<<<< HEAD
    serializes instances to a JSON file and deserializes
    JSON file to instances

    """

    __file_path = "file.json"
=======
    file storage
    """
    __file_path = "file.json"

>>>>>>> 281e15e5d5aa3ae94c715583453a3205c97157ff
    __objects = {}

    def new(self, obj):
        """
<<<<<<< HEAD
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

=======
        new
        """
        obj_cls_name = obj.__class__.__name__

        key = "{}.{}".format(obj_cls_name, obj.id)

        FileStorage.__objects[key] = obj

    def all(self):
        """
        alla
        """
>>>>>>> 281e15e5d5aa3ae94c715583453a3205c97157ff
        return FileStorage.__objects

    def save(self):
        """
<<<<<<< HEAD
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
=======

        """
        lobj = FileStorage.__objects

        objd = {}

        for obj in lobj.keys():
            objd[obj] = lobj[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(objd, file)

    def reload(self):
        """

        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    objd = json.load(file)

                    for key, value in objd.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**values)

                        FileStorage.__objects[key] = instance
>>>>>>> 281e15e5d5aa3ae94c715583453a3205c97157ff
                except Exception:
                    pass
