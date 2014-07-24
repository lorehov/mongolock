__version__ = '0.1'

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(name='mongolock',
      version=__version__,
      description='Python Mongodb based Distributed Lock',
      long_description=README,
      classifiers=[
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='lock mongo',
      author="Lev Orekhov",
      author_email="lev.orekhov@gmail.com",
      url="https://github.com/lorehov/mongolock",
      license="BSD",
      py_modules=['mongolock'],
      test_suite="test_mongolock",
      include_package_data=True,
      zip_safe=False,
      tests_require=['pytest>=2.6.0'],
      install_requires=[
          "mongodb>=2.4.2",
      ]
)
