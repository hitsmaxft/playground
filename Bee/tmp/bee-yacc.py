#!/usr/bin/python

import ply.yacc as yacc
import ply.lex as lex


tokens_op = ['EQ', 'GT', 'LT', 'GE', 'LE']
tokens = ['NODE', "NUMBER", "STRING", "OP", "EXPR", 'COMMENT']
tokens.extend(tokens_op)

t_ignore_COMMENT = r'\;.*'

t_NODE = r'[a-z.]+'

t_STRING = r'".*"'

t_OP = " = "

def t_NUMBER  (t):
    r'\d+'
    t.value = int(t.value)
    return t

def EXPR (t):
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

s="data.navigator.type=3"
#yacc.yacc()
#yacc.parse(s)
lexer = lex.lex()
lexer.input(s)
print(list(lexer))
