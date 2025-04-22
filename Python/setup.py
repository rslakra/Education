#
# Author: Rohtash Lakra
#
from setuptools import setup, find_packages

setup(
    name='pycli',
    version='0.1.0',
    description='Learning Python',
    url='https://github.com/rlakra-tinker/Python',
    author='Rohtash Lakra',
    author_email='rslakra.work@gmail.com',
    license='MIT',
    install_requires=['requests'],
    packages=find_packages(),
    entry_points=dict(
        console_scripts=[
            'pycli = pycli.main:main',
        ]
    ))
