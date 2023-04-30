#!/bin/env python
# -*- coding: utf-8 -*-

# GNU release project manager log
from .config import *
from logging import *

basicConfig(level = NOTSET,
                format="[%(levelname)s %(asctime)s '%(filename)s:%(lineno)d'] %(message)s",
                datefmt="%a, %d %b %Y %H:%M:%S")

Log = Logger.root
Log.setLevel(NOTSET)
