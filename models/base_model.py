#!/usr/bin/python3
"""
module
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Base class for other classes

    Attributes:
    id (str): A unique identifier for the instance
    created_at (datetime): Timestamp for instance creation
    updated_at (datetime): Timestamp for instance update
    """

    def __init__(self, *args, **kwargs):

        """

        """

        time = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())

            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

        models.storage.new(self)

    def save(self):
        """

        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """

        """
        sdict = self.__dict__.copy()
        sdict["__class__"] = self.__class__.__name__
        sdict["created_at"] = self.created_at.isoformat()
        sdict["updated_at"] = self.updated_at.isoformat()

        return sdict

    def __str__(self):
        """

        """
        classs = self.__class__.__name__
        return "[{}] ({}) {}".format(classs, self.id, self.__dict__)


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
