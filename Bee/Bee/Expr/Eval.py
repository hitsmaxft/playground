#!/bin/bash/python
# -*- coding: utf-8 -*-

__author__ = 'hitsmaxft'

import ply.lex as lex
import ply.yacc as yacc
import re

from Bee.Expr import Node


class Eval(object):


    def __init__(self, symbols):
        self.symbols = symbols
    def runStringOnce(self, rule, obj=None):

        def find_node_value(path):
            v = obj
            for n in path:
                if v == None:
                    return None
                v = v.get(n, None)
                if v == None:
                    return None
            return v

        tokens_op = ['REQ', 'EQ', 'GT', 'LT', 'GE', 'LE', 'IN']

        tokens = ["REGEX", 'NODE', "NUMBER", "STRING"]

        tokens.extend(tokens_op)

        #t_OP = r'\s*[+-\/=><]\s*'

        t_REQ = r'~'
        t_EQ = r'='
        t_GT = r'>'
        t_GE = r'>='
        t_LT = r'<'
        t_LE = r'<='
        t_IN = r'@'

        t_ignore = ' \t'

        t_ignore_COMMENT = r'\;.*'

        def t_error(t):
            print(t)

        def t_NODE(t):
            r'^[#]?[A-Za-z][A-Za-z0-9.*]+'
            #t.value = Node(t.value)

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

        def p_error(t): print("Syntax error at '%s'" % t.value)

        def p_expression_node(t):
            'expression : NODE'
            t[0] = t[1]

        def p_expression_number(t):
            'expression : NUMBER'
            t[0] = t[1]

        def p_expression_string(t):
            'expression : STRING'
            t[0] = t[1]

        def p_expression_regex(t):
            'expression : REGEX'
            t[0] = re.compile(t[1])

        def p_expression_eq(p):
            'expression : expression EQ expression'
            p[0] = p[1] == p[3]

        def p_expression_ge(p):
            'expression : expression GE expression'
            p[0] = p[1] >= p[3]

        def p_expression_gt(p):
            'expression : expression GT expression'
            p[0] = p[1] > p[3]

        def p_expression_lt(p):
            'expression : expression LT expression'
            p[0] = p[1] < p[3]

        def p_expression_le(p):
            'expression : expression LE expression'
            p[0] = p[1] <= p[3]

        def p_expression_in(p):
            'expression : expression IN expression'
            if isinstance(p[1], list):
                try:
                    p[1].index(p[3])
                    p[0] = True
                except ValueError:
                    p[0] = False
            else:
                p[0] = p[3] in p[1]

        def p_expression_reg_in(p):
            'expression : expression REQ REGEX'
            p[0] = re.match(p[3], p[1]) != None

        def raw_eval(l):
            l,op,r  = list(l)
            vleft = 12
            op = "__{}__".format(op.type.lower())
            vright = r.value

            op_method = getattr(vleft, op)
            return op_method(vright)
        l = lex.lex()
        l.input(rule)
        parser = yacc.yacc(write_tables=0)
        return parser.parse(rule)

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
