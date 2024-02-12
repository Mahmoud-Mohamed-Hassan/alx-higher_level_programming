#!/usr/bin/python3
"""models/base.py"""
import json


class Base:
    '''A representation of the base of our OOP hierarchy'''

    __nb__objects = 0

    def __init(self, id -None):
        '''Constructor'''
        if id is not None:
        '''give a unique id'''
            self.id = id
        else:
        '''if no id given give the next id'''
            Base._nb_objects += 1
            self.id = Base.__nb_objects 
