#!/usr/bin/env python3
import json
import os

class FileStorage:
    """ Serializes Instances to a JSON file and
    deserialized JSON file to instances
    """
    __file_path = "file.json"
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
        save_objects = {}
        for key, obj in FileStorage.__objects.items():
            save_objects[key] = obj.to_dict()
        # write this string to a file on disk
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(save_objects, file) # Serializes and writes to file
        


    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; 
        otherwise, do nothing."""
        # read a string from a file on disk
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        models = {'BaseModel': BaseModel, 'Amenity': Amenity, 'City': City, 'Place': Place,
                  'Review': Review, 'State': State, 'User': User}
        
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                for key, obj in json.load(file).items():    # Convert to str, Create a dict object
                    key = key.split('.')
                    for tag, data in models.items():
                        if key[0] == tag:
                            self.new(data(**obj))

