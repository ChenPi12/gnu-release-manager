#!/bin/env python
# -*- conding: utf-8 -*-

# Define Repo class
from .log import *
import json

class Repo(object):
    # Init Repo object
    def __init__(self, name:str, url:str = '*'):
        if(url == '*'):
            # Load json data to package
            self.load(name)
        else:
            # Set package info
            self.set(name, url)
    
    # Load Repo object from json data
    def load(self, jsondata:str):
        self.data = json.loads(jsondata)
    
    # Load Repo object from info
    def set(self, name:str, url:str, **kwargs):
        kwargs["name"] = name
        kwargs["url"] = url
        self.data = kwargs
    
    # Get data from key
    def get(self, key:str, default_value:str = None):
        r = self.data.get(key, default_value)
        if(r == None):
            raise KeyError(key)
        return r

    # Get Repo name
    def name(self):
        return self.get("name")
    
    # Get Repo url
    def url(self):
        return self.get("url")
    
    # Get Repo json info
    def get_json(self):
        return json.dumps(self.data)

    # To string
    def __str__(self, *args, **kwargs):
        return f"{self.__class__.__name__}({self.get_json()})"
    
    # Repr
    def __repr__(self, *args, **kwargs):
        return self.__str__()

