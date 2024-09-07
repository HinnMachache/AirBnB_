#!/usr/bin/env python3
from base_model import BaseModel

my_dict = {'name': 'Hinn', 'age': 90, 'id': 89869869869869}
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

my_new_model = BaseModel(**my_model_json)
print("New Model")
print(my_new_model)
latest_model = BaseModel(**my_dict)
print(latest_model)