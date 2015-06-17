# this file is used for installing 
# dependencies using pip 
# pip install --editable .

from setuptools import setup, find_packages

setup(
    name='genio',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click','requests'
    ],
    entry_points='''
        [console_scripts]
        genio=main:cli
    ''',
)

