#!/usr/bin/env python3
""" Review -> user Reviews on the BnB"""

from .base_model import BaseModel


class Review(BaseModel):
    """ Review Attributes"""
    place_id = ""
    user_id = ""
    text = ""
