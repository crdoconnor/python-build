from os import path, chdir
from sys import stdout, stderr, exit, argv
from subprocess import call

PYTHONBUILD_DIR = path.dirname(path.realpath(__file__))

def python_build(*args):
    pyenv_build_bin = path.join(PYTHONBUILD_DIR, "bin", "python-build")
    call([pyenv_build_bin] + list(args))

def run():
    python_build(*argv[1:])
