Gandit
======

Gandit是一个对Bandit进行二次开发的项目，旨在对python项目漏洞的扫描检测

Usage::

    $ python Gandit.py -h
    usage: Gandit [-h] [-r] [-a {file,vuln}] [-n CONTEXT_LINES] [-c CONFIG_FILE]
                  [-p PROFILE] [-t TESTS] [-s SKIPS] [-l] [-i]
                  [-f {csv,custom,html,json,screen,txt,xml,yaml}]
                  [--msg-template MSG_TEMPLATE] [-o [OUTPUT_FILE]] [-v] [-d]
                  [--ignore-nosec] [-x EXCLUDED_PATHS] [-b BASELINE]
                  [--ini INI_PATH] [--version]
                  [targets [targets ...]]

    Bandit - a Python source code security analyzer

    positional arguments:
      targets               source file(s) or directory(s) to be tested

    optional arguments:
      -h, --help            show this help message and exit
      -r, --recursive       find and process files in subdirectories
      -a {file,vuln}, --aggregate {file,vuln}
                            aggregate output by vulnerability (default) or by
                            filename
      -n CONTEXT_LINES, --number CONTEXT_LINES
                            maximum number of code lines to output for each issue
      -c CONFIG_FILE, --configfile CONFIG_FILE
                            optional config file to use for selecting plugins and
                            overriding defaults
      -p PROFILE, --profile PROFILE
                            profile to use (defaults to executing all tests)
      -t TESTS, --tests TESTS
                            comma-separated list of test IDs to run
      -s SKIPS, --skip SKIPS
                            comma-separated list of test IDs to skip
      -l, --level           report only issues of a given severity level or higher
                            (-l for LOW, -ll for MEDIUM, -lll for HIGH)
      -i, --confidence      report only issues of a given confidence level or
                            higher (-i for LOW, -ii for MEDIUM, -iii for HIGH)
      -f {csv,custom,html,json,screen,txt,xml,yaml}, --format {csv,custom,html,json,screen,txt,xml,yaml}
                            specify output format
      --msg-template        MSG_TEMPLATE
                            specify output message template (only usable with
                            --format custom), see CUSTOM FORMAT section for list
                            of available values
      -o [OUTPUT_FILE], --output [OUTPUT_FILE]
                            write report to filename
      -v, --verbose         output extra information like excluded and included
                            files
      -d, --debug           turn on debug mode
      --ignore-nosec        do not skip lines with # nosec comments
      -x EXCLUDED_PATHS, --exclude EXCLUDED_PATHS
                            comma-separated list of paths to exclude from scan
                            (note that these are in addition to the excluded paths
                            provided in the config file)
      -b BASELINE, --baseline BASELINE
                            path of a baseline report to compare against (only
                            JSON-formatted files are accepted)
      --ini INI_PATH        path to a .bandit file that supplies command line
                            arguments
      --version             show program's version number and exit

    自定义格式
    -----------------

    Available tags:

        {abspath}, {relpath}, {line},  {test_id},
        {severity}, {msg}, {confidence}, {range}

    Example usage:

        Default template:
        bandit -r examples/ --format custom --msg-template \
        "{abspath}:{line}: {test_id}[bandit]: {severity}: {msg}"

        Provides same output as:
        bandit -r examples/ --format custom

        Tags can also be formatted in python string.format() style:
        bandit -r examples/ --format custom --msg-template \
        "{relpath:20.20s}: {line:03}: {test_id:^8}: DEFECT: {msg:>20}"

        See python documentation for more information about formatting style:
        https://docs.python.org/3.4/library/string.html

    程序将载的插件列表:
    -----------------------------------------------

      B101  assert_used
      B102  exec_used
      B103  set_bad_file_permissions
      B104  hardcoded_bind_all_interfaces
      B105  hardcoded_password_string
      B106  hardcoded_password_funcarg
      B107  hardcoded_password_default
      B108  hardcoded_tmp_directory
      B109  password_config_option_not_marked_secret
      B110  try_except_pass
      B111  execute_with_run_as_root_equals_true
      B112  try_except_continue
      B201  flask_debug_true
      B301  pickle
      B302  marshal
      B303  md5
      B304  ciphers
      B305  cipher_modes
      B306  mktemp_q
      B307  eval
      B308  mark_safe
      B309  httpsconnection
      B310  urllib_urlopen
      B311  random
      B312  telnetlib
      B313  xml_bad_cElementTree
      B314  xml_bad_ElementTree
      B315  xml_bad_expatreader
      B316  xml_bad_expatbuilder
      B317  xml_bad_sax
      B318  xml_bad_minidom
      B319  xml_bad_pulldom
      B320  xml_bad_etree
      B321  ftplib
      B322  input
      B323  unverified_context
      B324  hashlib_new_insecure_functions
      B401  import_telnetlib
      B402  import_ftplib
      B403  import_pickle
      B404  import_subprocess
      B405  import_xml_etree
      B406  import_xml_sax
      B407  import_xml_expat
      B408  import_xml_minidom
      B409  import_xml_pulldom
      B410  import_lxml
      B411  import_xmlrpclib
      B412  import_httpoxy
      B501  request_with_no_cert_validation
      B502  ssl_with_bad_version
      B503  ssl_with_bad_defaults
      B504  ssl_with_no_version
      B505  weak_cryptographic_key
      B506  yaml_load
      B601  paramiko_calls
      B602  subprocess_popen_with_shell_equals_true
      B603  subprocess_without_shell_equals_true
      B604  any_other_function_with_shell_equals_true
      B605  start_process_with_a_shell
      B606  start_process_with_no_shell
      B607  start_process_with_partial_path
      B608  hardcoded_sql_expressions
      B609  linux_commands_wildcard_injection
      B701  jinja2_autoescape_false
      B702  use_of_mako_templates
      B703  TestCheck



将代码加入白名单
----------
如果一行代码触发了一个告警，但是该行经过审查，是一个误报或一些可以接受的其他原因。
该行可以用 ``＃nosec`` 进行标记，被标记的代码将不会触发任何告警。

例如，虽然这行代码虽然会导致Bandit报告安全问题，但被标记后，它将不会触发任何告警::

    self.process = subprocess.Popen('/bin/echo', shell=True)  # nosec


漏洞检测
-------------------
漏洞检测所用到的插件存放在plugins目录中。

漏洞检测插件用Python编写，并从plugins目录自被加载。
每个检测插件都可以检查一种或多种类型的Python语句。通过他们定义的标记，
来检查对应的Python语句的类型（例如：函数调用，
字符串，导入等）。


编写测试插件
-------------
To write a test:  
 - 在plugins目录中新建一个python文件，或者在已有的插件文件中进行二次开发.  
 - 合理的使用装饰器，标记你将要写的过滤插件用于检测什么类型的ast节点:  
   - @checks('Call')  
   - @checks('Import', 'ImportFrom')  
   - @checks('Str')  
 - 你创建的函数需要带一个参数“context”，它是你要检查的代码中某一个触发这个插件的节点的一个实例，通过它，你可以获取正在被检查的当前元素的信息。您还可以获取原始AST节点以获取更高级的属性值。请参阅context.py文件以获取更多信息。  
 
 - 下面举个call节点插件的例子

::

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
        print "FunctionDef:"+ast.dump(context.call_function_def)
        print "Call_name:"+context.call_function_name_qual
        print "DefName:"+context.call_function_def.name
        print "Call_args:"+str(context.call_args)
        print "severity_args:"+str(context.Function_dangerous_parameters)
        print "Show_all_call_args:"+str(context.Show_all_call_args)
        print "Call finish+++++"
        if "eval" == context.call_function_name:
            for call_arg in context.Call_dangerous_parameters:
                if call_arg in context.Function_dangerous_parameters:
                    print("eval warning")



@test.checks('Call')、@test.test_id('B703')分别代表，只有call节点类型的数据，才会触发此插件；此插件的id为'B703'.  
TestCheck方法是我们定义的规则插件，它有一个参数，名为context.  
在所有处理call节点的插件中，我们都可以用到如下的context属性，这些属性取决于这个节点对应的高级预处理器的处理.  
context属性如下：
			1.context.Call_dangerous_parameters: 这是一个list类型的数据，存放着这个call节点中可控的危险参数列表.  
			
			2.context.Function_dangerous_parameters: 这是个list类型的数据，存放着定义这个call节点的函数中所有可控的参数.  
			
			3.context.Show_all_call_args: 这是个list类型的数据，存放着这个call节点的所有参数. (注意！如果列表中的数据以'variable_'做前缀，那说明它是一个变量类型，变量名即为'variable_’后的值，如果无'variable_'修饰，那这个变量就是一个字符串或者是数字.eg:['variable_d', 'variable_a', 'c']).  
			
			4.context.call_function_def: 这是一个ast节点类型的数据，它存放着定义这个call的函数.  
			
			5.context.call_function_name: 此节点的函数名(eg:eval).  
			
			6.context.call_function_name_qual: 此节点的完整调用名(eg:os.popen).  
			
			7.node: 此节点的完整原始ast数据.
		 
简单的例子

::

	def test(a):  
		b = a[:]  
		d = 111  
		eval(b) 
context.Call_dangerous_parameters=['b']  

context.Function_dangerous_parameters=['a', 'b']  

context.Show_all_call_args=['variable_b']  

context.call_function_def=<_ast.FunctionDef object at 0x00000000040A19E8>  

context.call_function_name='eval'  

context.call_function_name_qual='eval'   

安装插件
----------------
- 在setup.cfg中找到 ``bandit.plugins = ``这行代码  
- 在下面配置你新增加的插件，写法仿照其他已有插件来写

::

    bandit.plugins =

        # bandit/plugins/FunctionTest.py
        TestCheck = bandit.plugins.FunctionTest:TestCheck
- 在setup.py中的entry_points列表中添加你新增的插件
::

    entry_points={'bandit.plugins': ['TestCheck = TestCheck','你的插件名 = setup.cfg中定义的名字']}


Gandit原理
----------------
Gandit流程图：  

![](http://gitlab.intra.nsfocus.com/gaoruiqiang/Gandit/raw/master/tree.png)  

Gandit是对Bandit的二次开发。具体的检测流程如下：  
   - 首先它会对要检测的python代码进行ast抽象语法树处理.
   - 接着会循环遍历生成的的ast树的叶子节点，并且分析这个叶子节点的ast类型.
   - 然后进入简单预处理器，将这个叶子节点进行一些简单的处理.
   - 紧接着寻找是否有针对这个节点类型的高级预处理器，（例如其中一个叶子节点类型是Call，会首先进行简单的预处理，然后寻找是否有下一层的visit_Call预处理器，如果有，就用visit_Call处理器再次处理），
   - 如果找到下一层的高级预处理器（如visit_Call/visit_Funcationdef等）时，叶子节点数据进入对应的高级预处理器再次针对性的进行数据加工与提取.
   - 当预处理工作全部完成后，根据该叶子节点的ast类型，加载所有对应装饰器装饰的插件（例如Call类型的叶子节点，就会遍历加载所有``@test.checks('Call')``的插件），将处理好的数据依次传递给这些插件.
   - 当传递进来的数据正好触发了某些/个插件的规则时，报出告警信息.
