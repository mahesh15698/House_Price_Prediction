from setuptools import setup
from typing import List

#Declaring Variables for setup functions
PROJECT_NAME= "hOUSING-Predictor"
VERSION="0.0.1"
AUTHOR ="Mahesh Jadhav"
DESCRIPTION ="This first Machine Leaning Deployment Project(Housing)"
PACKAGES =["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file return 
    This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()
        # requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        # if HYPHEN_E_DOT in requirement_list:
        #     requirement_list.remove(HYPHEN_E_DOT)
        # return requirement_list
    


 
setup(
name =PROJECT_NAME,
version=VERSION, 
author=AUTHOR,
description=DESCRIPTION,
packages= PACKAGES,
install_requires=get_requirements_list()

)

if __name__=="__main__":
    print(get_requirements_list())