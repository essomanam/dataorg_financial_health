from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    Cett fonction lit le fichier requirements.txt et retourne une liste des packages
    '''
    requirements = []
    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
name="dataorg_financial_health",
version="0.1.0",
author="essomanam",
author_email="essomanam23@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt"),
)