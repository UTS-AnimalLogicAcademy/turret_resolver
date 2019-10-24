# -*- coding: utf-8 -*-

name = 'turret_resolver'

version = '1.1.2'

authors = ['wen.tan',
           'ben.skinner',
           'daniel.flood']

requires = ['python']

def commands():
    env.PYTHONPATH.append('{root}/python')
    env.RESOLVE.set("{root}/bin/turret-resolver.sh")
