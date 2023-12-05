from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='MLProject',
version='0.0.1',
author='Bhavana',
author_email='saibhavanaatluri@gmail.com',
packages=find_packages(),
#for install_requires we can either give a list of packages needed or call a function get_requirements('requirement.txt')
##install_requires=['pandas','numpy','seaborn'] 
install_requires=get_requirements('requirements.txt')

)