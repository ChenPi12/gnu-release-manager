#!/bin/env python
# -*- coding: utf-8 -*-

# GNU Release Manager main

from tools import *
from threading import *
from queue import *

def update_libcache():
    pl = get_online_repo_list()
    _repos = []
    for repo in pl:
        _repos.append(repo.get_json())
    set_config(REPOS_CACHE, "remote", _repos)

def pull_all():
    _rs = get_config(REPOS_CACHE, "remote")
    repos = []
    for _r in _rs:
        repos.append(Repo(_r))
    
    repos_que = Queue()
    for repo in repos:
        repos_que.put(repo)
    
    def _pull(repos:Queue):
        while(not repos.empty()):
            repo = repos.get()
            name = repo.name()
            url = repo.url()
            git.clone(url, "repos", name)
    
    tpool = []
    for i in range(NPROC):
        tpool.append(Thread(target = _pull, args = (repos_que,)))
    for i in tpool:
        i.start()
    for i in tpool:
        i.join()
    

update_libcache()
pull_all()
