# -*- coding: utf-8 -*-

name = 'Shark'

version = '0.1'

description = 'Shark'

tools = ['launch']

requires = [
    "PySide",
    "maya",
    "VSCode",


]

authors=["Tristan GIANDORIGGIO"]

#build_command = 'python {root}/build.py {install}'

def commands():
    global env
    env.PATH.append('{this.root}/dist')
    env.PYTHONPATH.append('{this.root}')
