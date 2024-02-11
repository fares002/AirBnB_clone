#!/usr/bin/python3
"""
module
"""

import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """

    """

    __file_path = "file.json"

    __objects = {}

    def new(self, obj):
        """

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
                except Exception:
                    pass
