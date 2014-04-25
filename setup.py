#!/usr/bin/python
# vim: set expandtab tabstop=4 shiftwidth=4:

import os
from distutils.core import setup
from distutils.extension import Extension

czipfile_ext_modules = []
czipfile_build_ext = {}

# Attempt to compile from Cython if available; use the .c if not
try:
    from Cython.Distutils import build_ext
    czipfile_ext_modules.append('czipfile.pyx')
    czipfile_build_ext['build_ext'] = build_ext
except ImportError:
    from distutils.command.build_ext import build_ext
    print "cython not found, using previously-cython'd .c file."
    czipfile_ext_modules.append('czipfile.c')
    czipfile_build_ext['build_ext'] = build_ext

# Utility function to read the README file.  
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'czipfile',
    version = '1.0.0',
    author = 'Python distribution, modified by CJ Kucera',
    author_email = 'pez@apocalyptech.com',
    description = ('A replacement for the builtin zipfile module, with '
                   'fast, C-based zipfile decryption'),
    license = 'Python Software Foundation License',
    keywords = 'zipfile zip decryption',
    url = 'http://pypi.python.org/pypi/czipfile',
    long_description = read('README'),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Python Software Foundation License',
        ],
    ext_modules = [Extension('czipfile', czipfile_ext_modules)],
    cmdclass = czipfile_build_ext,
)
