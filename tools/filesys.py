#!/bin/env python
# -*- coding: utf-8 -*-

# GNU release project manager filesystem operates

from .log import *
from .config import *
import os
import shutil

SEP = os.path.sep

def mkdir(path:str):
    if(not os.path.isdir(path)):
        os.makedirs(path)
        Log.info(f"Make directory: {path}")
def rm(path:str, recurse:bool = True, force:bool = False):
    if(os.path.isdir(path) and recurse):
        shutil.rmtree(path, force)
    elif(os.path.exists(path)):
        os.remove(path)
    else:
        return
    flag = '-'
    if(recurse): flag += 'r'
    if(force): flag += 'f'
    if(flag == '-'): flag = ''
    else: flag = f"({flag})"
    Log.info(f"Remove{flag}: {path}")

def touch(path:str,data:bytes = b''):
    if(not os.path.exists(path)):
        f = open(path, "wb")
        dl = f.write(data)
        f.close()
        Log.info(f"Touch file {path} and write {dl} bytes.")
