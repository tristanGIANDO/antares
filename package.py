# -*- coding: utf-8 -*-

name = 'antares'

version = '0.1'

description = 'Asset Manager'

tools = ['launch']

requires = [



]

authors=["Tristan GIANDORIGGIO"]

#build_command = 'python {root}/build.py {install}'

def commands():
    global env
    # env.PATH.append('{this.root}/dist')
    env.PYTHONPATH.append('{this.root}')
