#!/bin/bash/python
# -*- coding: utf-8 -*-

__author__ = 'hitsmaxft'

#from .. import Request
#from Node import Node

import ply.lex as lex
import ply.yacc as yacc


tokens_op = ['EQ', 'GT', 'LT', 'GE', 'LE']

tokens = ['NODE', "NUMBER", "STRING", "PY_OP", "EXPR", 'COMMENT', 'LIST']

tokens.extend(tokens_op)


#t_OP = r'\s*[+-\/=><]\s*'
t_PY_OP = r'(has|in|equal)'

t_EQ = r'='
t_GT = r'>'
t_GE = r'>='
t_LT = r'<'
t_LE = r'<='

t_ignore = ' \t'

t_ignore_COMMENT = r'\;.*'

def t_error (t):
    print(t)

def t_NODE(t):
    r'^[#]?[a-z.*]+'
    #t.value = Node(t.value)
    t.value = 3
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#def t_STRING = r'".*"'
def t_STRING(t):
    r'".*"'
    t.value = t.value.strip('''"''')
    return t

def EXPR(t):
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_LIST(t):
    r'\(.*\)'
    v = t.value[1:-2].strip(' ')

    #XXX 注意递归性能
    l = lex.lex()
    l.input(v)

    t.value = [ tk.value for tk in list(l) ]
    return t

def p_expression_cmp(p):
    'expression : NODE EQ NUMBER'
    p[0] = p[1] == p[3]

def _eval(l):
    l,op,r  = list(l)
    vleft = 12
    op = "__{}__".format(op.type.lower())
    vright = r.value

    op_method = getattr(vleft, op)
    return op_method(vright)

def runStringOnce(rule):
    l = lex.lex()
    l.input(rule)
    parser = yacc.yacc()
    return parser.parse(rule)
    return _eval(l)

def run(rules, file_path):
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
        #print(dir(list(l)[0]))
if __name__ == '__main__':
    rule="data.*navigator.type = 3"
    print(runStringOnce(rule))
