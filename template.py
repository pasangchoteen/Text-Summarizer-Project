import os
from pathlib import Path
import logging #to log all the info during run time as well
#logging stream
logging.basicConfig(level= logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'textSummarizer'

list_of_files = [
    '.github/workflows/.gitkeep', 
    #.github used for deployment. like whenever you commit your code in github it will automatically take your code from github and do the deployment in the cloud 
    #.gitkeep is just an empty/hidden file which we will delete later after we create our actual EML file
    f'src/{project_name}/__init__.py', # for local package import operations
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile", #build one docker img of our src code and we'll do the deployment of the img in our PC2 machine in AWS
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

]

for filepath in list_of_files:
    filepath = Path(filepath) #to convert the filepath campatible with my OS
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating Emplty file: {filename}")

    else:
        logging.info(f"{filename} already exists")