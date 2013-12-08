import os
import sys
import warnings

from setuptools import setup, find_packages

version = '1.0.1'
description = open('README.txt', 'r').read()

setup(name='descartes',
      version=version,
      description="Use geometric objects as matplotlib paths and patches",
      long_description=description,
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: GIS'
      ],
      keywords='matplotlib gis geojson geometry',
      author='Sean Gillies',
      author_email='sean.gillies@gmail.com',
      url='http://bitbucket.org/sgillies/descartes/',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      )
