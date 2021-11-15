# test0.1
import ply.lex as lex
from my_utils import slurp
from pprint import PrettyPrinter


tokens = ("STR","COUNTRY", "CAPITAL", "CURRENCY", "LANGUAGE", "LEADER", "NEWLINE")
states = (
    ("capital", "exclusive"),
    ("currency", "exclusive"),
    ("language", "exclusive"),
    ("leader", "exclusive")
)
t_ANY_ignore = ","

def t_STR(t):
    r"[^,]+"
    t.type = "COUNTRY"
    t.lexer.begin("capital")
    return t

def t_capital_STR(t):
    r"[^,]+"
    t.type = "CAPITAL"
    t.lexer.begin("currency")
    return t

def t_currency_STR(t):
    r"[^,]+"
    t.type = "CURRENCY"
    t.lexer.begin("language")
    return t

def t_language_STR(t):
    r"[^,]+"
    t.type = "LANGUAGE"
    t.lexer.begin("leader")
    return t

def t_leader_LEADER(t):
    r"[^\n]+"
    t.type = "LEADER"
    t.lexer.begin("INITIAL")
    return t

def t_NEWLINE(t):
    r"\n"
    pass

def t_ANY_error(t):
    print(f"Unexpected token: {t.value[:10]}")
    exit(1)

# Montar o lexer com as tokens em cima
lexer = lex.lex()
# Ler o documento data
lexer.input(slurp("data"))

i = 0
for token in iter(lexer.token, None):
    if i < 5:
        i += 1
    else:
        # print teste
        # print(f"{token.value} <- {token.type}\t", end = '')
        print(f"{token.value}\t", end='')


