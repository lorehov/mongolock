__version__ = '1.3.4'

import sys

from pathlib import Path
from setuptools import setup
from setuptools.command.test import test as test_command

README = (Path(__file__).parent / "README.md").read_text()


class PyTest(test_command):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        test_command.initialize_options(self)
        self.pytest_args = ['src/test_mongolock.py']

    def finalize_options(self):
        test_command.finalize_options(self)
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
    long_description_content_type='text/markdown; charset=UTF-8',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
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
    python_requires=">=3.7,<4.0",
    extras_require={"test": ["pytest>=6"]},
    install_requires=["dnspython>=2.3.0", "pymongo>=4.1.1"]
)
