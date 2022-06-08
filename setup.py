#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import unicode_literals
from setuptools import setup

with open('README') as f:
    readme = f.read()

long_description = readme

setup(
    name='pydigest',
    version='1.8',
    description=('A Python library to aid in implementing HTTP Digest Authentication.'),
    long_description=long_description,
    long_description_content_type='text/plain',
    author='Akoha Inc.',
    author_email='adminmail@akoha.com',
    url='http://bitbucket.org/akoha/python-digest/',
    packages=['python_digest'],
    package_dir={'python_digest': 'python_digest'},
    install_requires=['six'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=True,
)
