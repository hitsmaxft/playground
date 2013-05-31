#!/bin/bash/python
# -*- coding: utf-8 -*-

import ply.lex as lex

from Expr import Node

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
    t.value = Node(t.value)
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
    print([(t.type, t.value) for t in l])
