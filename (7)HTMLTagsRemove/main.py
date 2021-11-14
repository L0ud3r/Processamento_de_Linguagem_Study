from my_utils import slurp
import ply.lex as lex
import sys

tokens = ("TEXT", "O_HEAD", "C_HEAD", "O_TAG", "NL")
in_header = False
number = [0]
title = ""


def t_C_HEAD(t):
    r"</[hH][1-6]>"
    global in_header
    in_header = False
    num = ".".join([str(x) for x in number])
    print(f"{num} | {title.strip()}")
    pass


def t_O_HEAD(t):
    r"<[hH][1-6][^>]*>"
    global in_header, number, title
    title = ""
    in_header = True
    level = int(t.value[2])
    while len(number) > level:
        number.pop()      # [1, 2] => [1]
    if level == len(number):
        number[-1] = number[-1] + 1
    elif level > len(number):
        number.append(1)    # [1]  => [1, 1]
    pass


def t_O_TAG(t):
    r"<[^>]+>"
    pass


def t_TEXT(t):
    r"[^<\n]+"
    if in_header:
        global title
        title += t.value.strip() + " "
    pass


def t_NL(t):
    r"\n"
    pass


def t_error(t):
    print(f"Unexpected token: {t.value[:10]}")
    exit(1)


lexer = lex.lex()
lexer.input(slurp("ply.html"))
lexer.token()

# FAZER COM NOME DO FILE NA CONSOLA

# se na consola o input for diferente de 2 propriedades (2 palavras)
# if len(sys.argv) != 2:
#    print("Filename Missing!")
#    exit(1)

# content = slurp(sys.argv[1])
# lexer = lex.lex()
# for token in iter(lexer.token, None):
#    print(token.value)
