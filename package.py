# -*- coding: utf-8 -*-

name = 'turret_resolver'

version = '2.0.0'

authors = ['wen.tan',
           'ben.skinner',
           'daniel.flood']

build_requires = ['python']

def commands():
    env.PYTHONPATH.append('{root}/python')
    env.RESOLVE.set("{root}/bin/turret-resolver.sh")
