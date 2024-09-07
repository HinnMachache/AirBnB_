#!/usr/bin/env python3
import json


class FileStorage:
    """ Serializes Instances to a JSON file and
    deserialized JSON file to instances
    """
    __file_path = ""
    __objects = {}

    def all(self) -> dict:
        """ returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """ Sets in __objects the obj with key
        <obj class name>.id
        """
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[obj_key] = obj 
        

    def save(self):
        """serializes __objects to the JSON
        file (path: __file_path)
        """
        # convert an instance to Python built in serializable data structure (list, dict, number and string)
        # convert this data structure to a string (JSON format, but it can be YAML, XML, CSV…) - for us it will be a my_string = JSON.dumps(my_dict)
        save_objects = json.dumps(FileStorage.__objects)
        # write this string to a file on disk
        with open(FileStorage.__file_path, 'w') as file:
            file.write(save_objects)
        


    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; 
        otherwise, do nothing."""
        # read a string from a file on disk
        try:
            with open(FileStorage.__file_path, 'r') as file:
                reload_objects = file.read()
            # convert this string to a data structure.
            FileStorage.__objects = json.loads(reload_objects)
            # convert this data structure to instance
            raise FileNotFoundError
        except FileNotFoundError:
            print("File Specified not found. Please check filename and try again")

