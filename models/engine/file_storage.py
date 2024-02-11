#!/usr/bin/python3
"""
module
"""

import json
import os
from models.base_model import BaseModel
from models.user import user




class fileStorage:
    """
    file storage
    """
    __file_path = "file.json"

    __objects = {}
    
    def new(self, obj):
        """
        new
        """
        obj_cls_name = obj.__class_._name__

        key = "{}.{}".format(obj_cls_name, obj.id)

        fileStorage.__objects[key] = obj

    def all(self):
        """
        alla
        """
        return fileStorage.__objects
