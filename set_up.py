# this file is used for setting up 
# build 
# python set_up.py py2app

from setuptools import setup, find_packages

APP = ['main.py'] #
DATA_FILES = []
OPTIONS = {'argv_emulation': True}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)
