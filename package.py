# -*- coding: utf-8 -*-

name = 'turret_resolver'

version = '0.0.3'

authors = ['wen.tan',
           'ben.skinner',
           'daniel.flood']

build_requires = ['python']

def commands():
    env.PYTHONPATH.append('{root}/python')
