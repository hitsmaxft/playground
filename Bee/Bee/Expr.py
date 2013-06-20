#!/bin/bash/python
# -*- coding: utf-8 -*-
from Bee import BeeLang
import ply.lex as lex
import ply.yacc as yacc

__author__ = 'hitsmaxft'

class Wrapper(object):
    """
    值包装, 用于特殊类型运算
    """

    def __init__(self, v=None):
        self._v = v
        self._isNode = False

    def __len__(self):
        """len()"""
        pass

    def __dir__(self):
        pass

    def __eq__(self, v):
        """=="""
        pass

    def __ge__(self, v):
        """>="""
        pass

    def __le__(self, v):
        """<="""
        pass

    def __ne__(self, v):
        """!="""
        pass

    def __ne__(self, v):
        """!="""
        pass

class Node(object):
    """
    节点类型, 暂是不需要
    在语法解析阶段做好节点取值
    """

    def __init__(self, path):

        self._path = path
        #self._v = query(path)

    def parse(expr):
        """


        :return:
        """
        return expr

    def __len__(self):
        """
        检测节点值的长度 如果节点类型不是数组, 则返回错误

        :return: int|None
        """

        if (isinstance(self._getV(), dict) or
                isinstance(self._getV(), list)):
            return len(self._getV())
        return None

    def _getV(self):
        return self.v
        pass



class Query(object):
    """
    针对节点查寻的一个工具类. 用于解析和定位节点类型/值等
    """
    t_node = r"([a-z]+.)?[a-z]+"

    def is_node(path):
        """

        """
        return True
        pass

    def is_node_get_len(path):
        pass

    def is_node_get_keys(path):
        pass

    def is_node_get_int(path):
        pass

    def __init__(self, url, data):
        self._url = url
        self._d = data
        pass

    #查寻节点
    def query(self, ind=""):
        """
        :param ind: string
        """
        node_path = ind.split(".")
        node_ind = self._d
        if node_path:
            while 1:
                cur = node_path.pop()
                if not cur or cur not in node_ind:
                    return Wrapper(None)
                else:
                    pass

    def check_path(self, path):
        pass

    def _data(self):
        return {
            'data': {
                'nav': {
                'type': 3,
                'cat': ['13', '1512'],
                'prop': None
                },
                'headCrumb': {
                    'cat': '15'
                }
            },
            'log':None,
            'config':None
        }

class Eval(object):
    """
    脚本主要运行部分
    """

    def __init__(self, data=None, debug=0, node_prefix=None):
        """
        初始化数据以及上下文
        """
        self.data=data
        self.debug = debug
        self.prefix = node_prefix if None != node_prefix else ""
        self.lex = lex.lex(debug=debug, module=BeeLang)
        self.parser = yacc.yacc(debug=debug, module=BeeLang)

    def runScript(self, rule, obj=None):
        pass

    def raw_eval(l):
        l,op,r  = list(l)
        vleft = 12
        op = "__{}__".format(op.type.lower())
        vright = r.value

        op_method = getattr(vleft, op)
        return op_method(vright)

    def compress(self, rules="", data=None):
        """
        包装好脚本和数据, 注入全局变量
        """
        if None == data:
            data = self.data
        if type(data) != str:
            import json
            data = json.dumps(data)
        script = rules
        if len(self.prefix)>0:
            script=u"~PREFIX:{}\n{}".format(self.prefix, script)
        return u"~JSON:{}\n{}".format(data.encode("utf-8"), script)

    def runStringOnce(self, rules, data=None):
        """
        执行脚本
        """
        script=self.compress(rules, data)
        #self.lex.input(script)
        return self.parser.parse(script, debug=self.debug)

    def runTest(rules, file_path):
        '''
        >>>run()
        '''
        samples = [
            """data.*navigator.type = 3""",
            """data.*navigator.type > 3""",
            """data.*navigator.type >= 3""",
            """data.*navigator.type >= 3""",
            '''data.*navigator.prop has "500302"''',
            '''data.*navigator.prop in ( 3 12 "222" )''',
            ]
        for s in samples:
            l = lex.lex()
            l.input(s)
            print(dir(list(l)[0]))
