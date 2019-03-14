# -*- coding:utf-8 -*-
import os,sys
'''
d = os.path.dirname('.')
abspath = os.path.abspath(d)
parent_path  = os.path.dirname(abspath)
dirs  = os.path.dirname(parent_path)
sys.path.append(dirs)
from bandit.core import config
print dirs
'''

parent_path = os.path.dirname(os.getcwd())
sys.path.append(os.path.dirname(parent_path))
from bandit.core import config1

'''
dirs = os.path.join( os.path.dirname(os.getcwd()))
sys.path.append(dirs)
'''