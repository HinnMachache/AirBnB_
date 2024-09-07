#!/usr/bin/env python3
import datetime as dt
from typing import Any
from uuid import uuid4
from .engines import storage
""" The Base Model Class -> Super Class to other storage classes
"""

class BaseModel:
    """ Base Model Class
    """
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            for (key, value) in kwargs.items():
                if key != '__class__':
                    if key in ['created_at' , 'updated_at']:
                        value = dt.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = dt.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
    

    def __setattr__(self, name: str, value: Any) -> None:
        """ Over riding updated_time"""
        super().__setattr__(name, value)
        if name != 'updated_at':
            self.updated_at = dt.datetime.now()

    def __str__(self) -> str:
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """ Save Operation"""
        self.updated_at = dt.datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """ Dictionary Representation of the Class"""
        created_time_str = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        updated_time_str = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        class_dict = self.__dict__.copy()
        class_dict['__class__'] = self.__class__.__name__
        if 'created_at' in class_dict:
            class_dict['created_at'] = created_time_str
        if 'updated_at' in class_dict:
            class_dict['updated_at'] = updated_time_str
        return class_dict

