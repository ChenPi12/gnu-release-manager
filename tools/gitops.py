#!/bin/env python
# -*- coding: utf-8 -*-

# Git operates

from .config import *
from .log import *

import git as _git
import os
from pathlib import *
from urllib.parse import *

class git:
    @staticmethod
    def clone(url:str, path:str, basename:str = "*"):
        Log.info(f"Cloning {url} into '{path}{os.path.sep}{basename}'")
        urlp = urlparse(url)
        if(basename == "*"):
            basename = os.path.basename(urlp.path)
        path = Path(path, basename).absolute()
        cmd = f"\"{GIT}\" clone -v --progress -- \"{url}\" \"{str(path)}\""
        Log.info(f"Running command: {cmd}")
        assert os.system(cmd) == 0
        return _git.Repo(str(path))