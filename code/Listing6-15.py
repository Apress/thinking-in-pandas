import pyximport

pyximport.install(language_level=3)

from distutils.core import setup

from Cython.Build import cythonize


setup(ext_modules=cythonize("percentileofscore.pyx"))
