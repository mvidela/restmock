from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='restmock',
      version=version,
      description="A REST mock factory",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='rest, mock, documentation',
      author='Mariano Videla',
      author_email='mvidela@2vtechnology.com',
      url='www.2vtechnology.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
