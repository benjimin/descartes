from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='descartes',
      version=version,
      description="Use geometric objects as matplotlib paths and patches",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='matplotlib gis geometry',
      author='Sean Gillies',
      author_email='sean.gillies@gmail.com',
      url='http://bitbucket.com/sgillies/descartes',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
