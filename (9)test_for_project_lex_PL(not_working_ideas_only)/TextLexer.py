# TextLexer.py

import ply.lex as plex
from my_utils import slurp

class Reader:

    tokens = ("COUNTRY", "CAPITAL", "CURRENCY", "LANGUAGE", "LEADER", "LIXO")
    states = (
        ("capital", "exclusive"),
        ("currency", "exclusive"),
        ("language", "exclusive"),
        ("leader", "exclusive"),
        ("lixo", "exclusive")
    )

    t_ignore = ""

    exp_geral_str = r"[^,]+"

    def __init__(self):
        self.lexer = None

    @staticmethod
    def builder(**kwargs):
        obj = Reader()
        obj.lexer = plex.lex(module=obj, **kwargs)
        return obj

    def output(self, filename):
        # Ler ficheiro e armazenar em memoria
        self.lexer = plex.lex()
        lexer.input(slurp("ply.html"))
        # Lexer le variavel com dados do file e faz a separacao
        lexer.token()

    @TOKEN(exp_geral_str)
    def t_country_STR(self, t):
        t.type = "COUNTRY"
        t.lexer.begin("capital")
        return t

    @TOKEN(exp_geral_str)
    def t_capital_STR(self, t):
        t.type = "CAPITAL"
        t.lexer.begin("currency")
        return t

    @TOKEN(exp_geral_str)
    def t_currency_STR(self, t):
        t.type = "CURRENCY"
        t.lexer.begin("language")
        return t

    @TOKEN(exp_geral_str)
    def t_language_STR(self, t):
        t.type = "LANGUAGE"
        t.lexer.begin("leader")
        return t

    def t_leader_STR(self, t):
        r"[^\n]+"
        t.type = "LEADER"
        t.lexer.begin("lixo")
        return t

    def t_lixo_LIXO(self, t):
        r"\n"
        t.lexer.begin("INITIAL")
        return t

