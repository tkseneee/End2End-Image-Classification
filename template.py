# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 11:13:16 2024

@author: tksen
"""
#tksendevops@777
#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

#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

#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

#git remote set-url origin https://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@github.com/tkseneee/End2End-Image-Classification.git

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"


]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")




