from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    return the requirement lists

    '''
    requirements = []
    constant = '-e .'
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if constant in requirements:
            requirements.remove(constant)
    
    return requirements


setup(
    name="Machine Learning Project",
    version="0.0.1",
    author="Sathishkumar Pari",
    author_email="sathishpari27@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)