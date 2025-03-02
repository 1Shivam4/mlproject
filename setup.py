from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requriements
    '''
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        ''' 
        Do not include -e . as it serves the setup.py file to 
        run automatically.
        '''
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        return requirements
        

setup(
    name='mlproject',
    version='0.0.1',
    author='shivam',
    author_email='shivamsahni507@gmail.com',
    packages=find_packages(),
    install_requries=get_requirements('requirements.txt')
)