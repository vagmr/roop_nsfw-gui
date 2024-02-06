#!/usr/bin/env python3

from roop import core
from roop import globals

if __name__ == '__main__':
    for attr in dir(globals):
    # 过滤掉内置的属性和方法
     if not attr.startswith('__'):
        print(f'{attr}: {getattr(globals, attr)}')
    core.run()
