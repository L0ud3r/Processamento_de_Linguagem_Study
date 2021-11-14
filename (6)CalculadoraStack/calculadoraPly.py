# calculatorPly.py

import ply.lex as lex
from main import Calculator

class Calculadora:

    def __init__(self):
        self.lexer = None

    def initialize(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

    # tokens
    tokens = ("NUM", "ADD", "SUB", "DIV", "MUL")

    def t_NUM(t):
        r"""[0-9]+(\.[0-9]+)?"""
        t.value = float(t.value)
        return t

    def t_ADD(t):
        r"ADD|add"
        t.value = Calculator.add
        return t

    def t_SUB(t):
        r"MINUS|minus"
        t.value = Calculator.sub
        return t

    def t_DIV(t):
        r"DIV|div"
        t.value = Calculator.div
        return t

    def t_MUL(t):
        r"MUL|mul"
        t.value = Calculator.mul
        return t


    # Caracteres ignorados
    t_ignore = " "

    def t_error(t):
        print(f"Unexpected input: {t.value[:10]}")
        exit(1)






