from setuptools import setup, find_packages
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='falgopy',
    version='1.0.0',    
    description='A powerful algorithms package',
    
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='',
    author='Zohar franco',
    author_email='',
    packages=find_packages(), 
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
    ],
    keywords='CS data data structures algorithms algo',
)
