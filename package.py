# -*- coding: utf-8 -*-
import env

name = 'antares'

version = '0.3'

description = 'Pipeline Manager'

tools = ['launch']

requires = [



]

authors=["Tristan GIANDORIGGIO"]

#build_command = 'python {root}/build.py {install}'

def commands():
    global env
    # env.PATH.append('{this.root}/dist')
    env.PYTHONPATH.append('{this.root}')
