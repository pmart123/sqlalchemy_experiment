#!/usr/bin/env python

from setuptools import find_packages, setup

setup(name='sqlalchemy_experiment',
      packages=find_packages(),
      version='0.0.1',
      description='sqlalchemy test for ddl formatting.',
      url='https://github.com/pmart123/sqlalchemy_experiment',
      classifiers=['Private :: Do Not Upload'],
      author='Philip Martin',
      author_email='philip.martin2007@gmail.com',
      install_requires=list(open('requirements.txt').read().strip().split('\r\n')),
      zip_safe=False)
