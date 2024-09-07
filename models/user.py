#!/usr/bin/env python3
""" User -> Class containing User Info"""
from .base_model import BaseModel


class User(BaseModel):
    """ User Attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""