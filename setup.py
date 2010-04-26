import os
import sys
import warnings

try:
    from distribute_setup import use_setuptools
    use_setuptools()
except:
    warnings.warn(
    "Failed to import distribute_setup, continuing without distribute.", 
    Warning)

from setuptools import setup, find_packages

version = '1.0'
description = open('README.txt', 'rb').read()

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
