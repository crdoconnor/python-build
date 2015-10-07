# -*- coding: utf-8 -*
from setuptools import find_packages
from setuptools import setup
import codecs
import sys
import os


def read(*parts):
    # intentionally *not* adding an encoding option to open
    # see here: https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts), 'r').read()

setup(name="python-build",
      version="0.2.4",
      description="Tool to download and build python based upon pyenv.",
      long_description=read('README.rst'),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Testing',
          'Topic :: Software Development :: Libraries',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
      ],
      keywords='build download install python versions',
      author='Colm O\'Connor',
      author_email='colm.oconnor.github@gmail.com',
      license='MIT',
      install_requires=[],
      packages=find_packages(exclude=[]),
      package_data={},
      zip_safe=False,
      entry_points=dict(console_scripts=['python-build=python_build:build.run',]),
      include_package_data=True,
)

