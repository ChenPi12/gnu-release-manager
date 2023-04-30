#!/bin/env python
# -*- coding: utf-8 -*-

# Init tools
from .config import *
from .getlist import *
from .log import *
from .repo import *
from .gitops import *
from .filesys import *

REPOS_CACHE = f"config.d{SEP}libs.json"

mkdir("repos")
mkdir("config.d")
touch(REPOS_CACHE, b"{}")

def load_config(file:str):
    f = open(file, "rt", encoding="utf-8")
    r = json.load(f)
    f.close()
    return r

def get_config(file:str, key:str, defval:str = None): # type: ignore
    r = load_config(file).get(key, defval)
    if(r == None):
        raise KeyError(key)
    return r

def set_config(file:str, key:str, val):
    cfg = load_config(file)
    cfg[key] = val
    f = open(file, "wt", encoding="utf-8")
    json.dump(cfg,f)
    Log.info("Config saved.")
