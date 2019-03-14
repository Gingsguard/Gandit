# -*- coding:utf-8 -*-
# Author:Ging'sGuard


import ast
import os, sys

'''import bandit'''
parent_path = os.path.dirname(os.getcwd())
sys.path.append(os.path.dirname(parent_path))

import bandit
from bandit.core import test_properties as test
@test.checks('Call')
@test.test_id('B703')
def TestCheck(context):
    print "Function_dangerous_parameters:"+str(context.Function_dangerous_parameters)
    #print "FunctionDef:"+ast.dump(context.call_function_def)
    print "Call_name:"+context.call_function_name_qual
    print "DefName:"+context.call_function_def.name
    print "Call_args:"+str(context.call_args)
    print "severity_args:"+str(context.Function_dangerous_parameters)
    print "Show_all_call_args:"+str(context.Show_all_call_args)
    print "Call finish+++++"
    if "popen" in context.call_function_name:
        for call_arg in context.call_args:
            if call_arg in context.Function_dangerous_parameters:
                print "fuck!!!!"
                return bandit.Issue(
                    severity=bandit.HIGH,
                    confidence=bandit.HIGH,
                    text="find eval call."
                    )
            else:
                print "nothing!!!!"
                return bandit.Issue(
                    severity=bandit.MEDIUM,
                    confidence=bandit.MEDIUM,
                    text="find eval call."
                    )

