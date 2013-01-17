"""
Cython setup file.
Cythonize high-performance stuff, actually only module Math (please don't worry, I'll do more hacks).
ALWAYS EXECUTE BEFORE RUNNING APPLICATION!
"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [
                   Extension("mathf", ["mathf.pyx"])]
)

