#!/usr/bin/env python

from distutils.core import setup

# ref: https://docs.python.org/3/distutils/setupscript.html#

setup(
    name='Distutils',
    version='1.0',
    description='Python Distribution Utilities',
    author='Greg Ward',
    author_email='gward@python.net',
    url='https://www.python.org/sigs/distutils-sig/',
    packages=[
        'distutils', 
        'distutils.command'
    ],
)