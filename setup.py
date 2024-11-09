# This is the setup configuration for the jgit package.
# It specifies the package name, version, and the packages included.
# The entry_points section defines a command line script 'jgit' that
# will execute the main function in jgit.cli module.

from setuptools import setup

setup(name = 'jgit',
      version = '1.0',
      packages = ['jgit'],
      entry_points = {
          'console_scripts' : [
              'jgit = jgit.cli:main'
          ]
      })

