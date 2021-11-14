# App que lê formulas quimicas

import ply.lex as lex

# Tokens sao os alfabetos (neste caso SQ -> letras das formulas quimicas e NR -> sao os numeros de atomos)
tokens = ("SQ", "NR")

# Podemos definir aqui as possiveis palavras ou numa função onde se pode tomar mais opcoes e propriedades
t_SQ = r"Cl|C|H|O"
t_ignore = " "

# Definição de cada alfabeto

# def t_SPC(t):
#     r"[ ]"
#     pass


def t_NR(t):
    r"[0-9]+"
    t.value = int(t.value)
    return t


def t_error(t):
    print(f"Token not recognized: {t}")
    exit(1)


lexer = lex.lex()
lexer.input("H2O HCl")
for t in iter(lexer.token, None):
    print(t)
