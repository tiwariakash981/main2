from setuptools import find_packages,setup
from typing import List 
from src.logger import logging



HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    ye requirements.txt ka sara content dekhega
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name = 'mlproject',
version='0.0.1',
author = 'krish',
author_email = 'tiwariakash981@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')

)