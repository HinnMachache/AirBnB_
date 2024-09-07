#!/usr/bin/env python3
""" Class Place -> Exact Place where BnB is at
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place attributes"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""