from subprocess import check_output, check_call
from sys import stdout, stderr, exit, argv, platform
from os import path, chdir, environ
import copy


PYTHONBUILD_DIR = path.dirname(path.realpath(__file__))


def python_build(*args):
    # Get a copy of system environment vars, so it can be modified accordingly and passed on.
    environment_vars = copy.copy(environ)

    # Mac OS special config from https://github.com/yyuu/pyenv/wiki/Common-build-problems
    #if platform == "darwin":
    #    osx_version = check_output(["sw_vers", "-productVersion"]).decode('utf8').replace('\n', '')
    #    if "10.9" in osx_version or "10.10" in osx_version:
    #        sdk_path = check_output(["xcrun", "--show-sdk-path"]).decode('utf8').replace('\n', '')
    #        environment_vars.update({"CFLAGS": "-I{}/usr/include".format(sdk_path)})

    # Get the full path to the python-build executable
    pyenv_build_bin = path.join(PYTHONBUILD_DIR, "bin", "python-build")

    # Pass on environment vars and args to pyenv build script
    check_call([pyenv_build_bin] + list(args), env=environment_vars)


def run():
    python_build(*argv[1:])
