#!/bin/bash/python
# -*- coding: utf-8 -*-
import re
import json

#data register
symbol_table = {'nodes':None}

#help for resolving node value
def find_node_value(path):
    v = symbol_table.get('nodes')
    for n in path:
        if v == None:
            return None
        v = v.get(n, None)
        if v == None:
            return None
    return v

#token list for lexer
tokens = ['REQ', 'EQ', 'GT', 'LT', 'GE', 'LE', 'IN',"REGEX", 'NODE', "NUMBER", "STRING", 'JSON', 'SEP']

precedence = (
    ('nonassoc','REQ', 'EQ', 'GT', 'LT', 'GE', 'LE', 'IN'),
)


## rule for tokens

t_REQ = r'~'
t_EQ = r'='
t_GT = r'>'
t_GE = r'>='
t_LT = r'<'
t_LE = r'<='
t_IN = r'@'
t_ignore = ' \t'
t_ignore_COMMENT = r'\;.*'
t_SEP = r'[;]'

def t_JSON(t):
    r'^~JSON:.*'
    symbol_table['nodes'] = json.loads(t.value[6:])
    return None

def t_error(t):
    #print(t)
    pass

def t_NODE(t):
    r'[#]?[A-Za-z][A-Za-z0-9.*]+'
    count_len = False
    if t.value[0] == "#":
        count_len = 1
        value = t.value[1:].split(".")
    else:
        value = t.value.split(".")

    node_value = find_node_value(value)
    if node_value == None:
        t.value = 0
        return t
    if count_len:
        t.value = len(node_value)
    else:
        t.value = node_value
    return t

def t_NUMBER(t):
    r'(\d+)'
    t.value = int(t.value)
    return t

#def t_STRING = r'".*"'
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value.strip('''"''')
    return t

def t_REGEX(t):
    r'r".*"'
    t.value = eval(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def p_error(t):
    if hasattr(t, 'value'):
        value = t.value
    else:
        value = 'undefined'

    if hasattr(t, 'lexer'):
        line_on  = t.lexer.lineno
    else:
        line_no = 'unknow line'

    print("Syntax error at '%s' in %s" % (value, line_no))

def p_statement(t):
    """
    statement : expression
    """
    t[0] = t[1]

def p_statement_recursive(t):
    """
    statement : expression statement
    """
    t[0] = t[1] and t[2]

def p_factor_value(t):
    '''
    factor : NODE
           | NUMBER
           | STRING
    '''
    t[0] = t[1]


def p_factor_regex(t):
    'factor : REGEX'
    t[0] = re.compile(t[1])

def p_factor_miexd(p):
    '''
    expression : factor EQ factor
                  | factor GE factor
                  | factor GT factor
                  | factor LE factor
                  | factor LT factor
    '''
    if p[2] == "=":
        p[0] = p[1] == p[3]
    elif p[2] == '>=' :
        p[0] = p[1] == p[3]
    elif p[2] == '>' :
        p[0] = p[1] > p[3]
    elif p[2] == '<=' :
        p[0] = p[1] <= p[3]
    elif p[2] == '<' :
        p[0] = p[1] < p[3]

def p_factor_in(p):
    'expression : factor IN factor'
    if isinstance(p[1], list):
        try:
            p[1].index(p[3])
            p[0] = True
        except ValueError:
            p[0] = False
    else:
        p[0] = p[3] in p[1]

def p_factor_reg_in(p):
    'expression : factor REQ REGEX'
    p["123"]=22
    print(dir(p["123"]))
    p[0] = re.match(p[3], p[1]) != None