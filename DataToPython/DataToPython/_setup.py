# -*- coding: UTF-8 -*-
from distutils.core import setup, Extension
MOD = 'core'      #库：core 源文件：_core.c
setup(name=MOD, ext_modules=[Extension(MOD, sources=['_core.c'])]) 