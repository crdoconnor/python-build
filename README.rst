Python-Build
============

BuildPython is a python library to download and build a specified version of python
into a specified directory.

That's it.

The code is basically derived from pyenv but provides a bit of a nicer wrapper.

It was built for use with http://hitchtest.com/ so that you can test the same code with multiple versions of python.


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
