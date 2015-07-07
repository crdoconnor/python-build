Python-Build
============

BuildPython is a python library to download and build a version of python
into a specified directory.

That's it.

The code herein is basically derived from pyenv.

It can substitute for virtualenv.


Use
===

Install::

  $ pip install python-build

Use in python::

  >>> import python_build
  >>> python_build.python_build("2.7.3", "/home/user/projectdirectory/py273")

Use outside of python::

  $ python-build 2.7.3 /home/user/projectdirectory/py273

Help::

  $ python-build --help
