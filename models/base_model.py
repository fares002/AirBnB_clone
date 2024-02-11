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
<<<<<<< HEAD
        """
        Initializes new instance of the BaseModel class
        Args:
            *args: Variables length argument list (unused)
            **kwargs: Arbitrary keyword arguments to create the instance
        """

        time_format = "%Y-%m-%dT%H:%M:%S.%f"

=======
        time = "%Y-%m-%dT%H:%M:%S.%f"
>>>>>>> 281e15e5d5aa3ae94c715583453a3205c97157ff
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
<<<<<<< HEAD

=======
        
>>>>>>> 281e15e5d5aa3ae94c715583453a3205c97157ff
        models.storage.new(self)

    def save(self):
        """

        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """

        """
<<<<<<< HEAD
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_att"] = self.created_at.isoformat()
        
        return inst_dict

    def __str__(self):
        """
        _summary_
        """

        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
    
    
    
    
=======
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


>>>>>>> 281e15e5d5aa3ae94c715583453a3205c97157ff
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
