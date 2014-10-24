__version__ = '1.3.1'

import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ['src/test_mongolock.py']

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='mongolock',
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
    keywords='lock mongodb',
    author="Lev Orekhov",
    author_email="lev.orekhov@gmail.com",
    url="https://github.com/lorehov/mongolock",
    license="BSD",
    package_dir={'': 'src'},
    py_modules=['mongolock'],
    cmdclass={'test': PyTest},
    test_suite="test_mongolock",
    include_package_data=True,
    zip_safe=False,
    tests_require=['pytest>=2.6.0'],
    install_requires=["pymongo>=2.6.0"]
)
