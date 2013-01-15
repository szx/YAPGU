"""
Cythonize high-performance stuff, actually only module Vector (please don't worry, I'll do more hacks).
"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [
                   Extension("Vector", ["Vector.pyx"])]
)

