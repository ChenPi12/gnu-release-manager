#!/bin/env python
# -*- coding: utf-8 -*-

# Get repo list from GNU Savannah
from .repo import *
import requests

pl_url = "https://git.savannah.gnu.org/git/project-list"
repo_url_fmt = "https://git.savannah.gnu.org/git/%s"

def get_online_repo_list():
    data = requests.get(pl_url).content.decode(CHARSET)
    repos = []
    for i in data.split("\n"):
        i = i.strip()
        repo = Repo(i.replace(".git","").replace("/","_"), repo_url_fmt % i)
        if(repo.name() == ""):
            continue
        repos.append(repo)
    Log.info(f"Get gnu repos list from {pl_url}: {len(repos)} repos.")
    return repos

if __name__ == '__main__':
    opl = get_online_repo_list()
    for repo in opl:
        print(repo)
