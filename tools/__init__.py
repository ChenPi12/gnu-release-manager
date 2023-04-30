#!/bin/env python
# -*- coding: utf-8 -*-

# Init tools
from .config import *
from .getlist import *
from .log import *
from .repo import *
from .gitops import *
from .filesys import *

mkdir("repos")
mkdir("config.d")
touch(f"config.d{SEP}config.conf",b"{}")