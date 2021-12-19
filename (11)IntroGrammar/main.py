# Programa interpretar simbolos lógicos

# Adicionar biblioteca ply
import ply.lex as plex


# criação da Class lexer que vai interpretar o texto
class Lexer:
    # Tokens do nosso Lexer
    tokens = ("not", "and", "or", "true", "false")
    # Simbolos equacionais
    literals = ['(', ')', '$']
    # t_ignore do Lexer, ignora espaços
    t_ignore = " "

    # Inicializador de Objeto
    def __init__(self):
        self.lexer = None

    # Builder do objeto
    def builder(self, expression, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)
        self.lexer.input(expression)

    # Função de leitura e armazenamento de valor lógico ou bolleano
    def t_str(self, t):
        r"false|true|and|not|or"
        t.type = t.value
        return t

    # Função de retorno de token (POR REVER)
    def token(self):
        token = self.lexer.token()
        if token is None:
            return token
        else:
            return token.type

    # Função de erro
    def t_error(self, t):
        print(f"Unexpected input: {t.value[:15]}")
        exit(1)


# Classe de gramatica
class Grammar:

    # Inicializador de Objeto
    def __init__(self, expression):
        self.lexer = Lexer()
        self.lexer.builder(expression + "$")
        self.symbol = self.lexer.token()

    # Função do símbolo inicial
    # Z -> B | $
    def rec_Z(self):
        if self.symbol in ["true", "false", "not", '(']:
            # Exercutar o início da expressão + o fim "$"
            return self.rec_B() and self.rec_terminal("$")
        else:
            return False

    # Funções de interpretação de cada Símbolo nao Terminal
    # B -> T B'
    def rec_B(self):
        if self.symbol in ["true", "false", "not", '(']:
            return self.rec_T() and self.rec_Bl()
        else:
            return False

    # T -> F T'
    def rec_T(self):
        if self.symbol in ["true", "false", "not", '(']:
            return self.rec_F() and self.rec_Bl()
        else:
            return False

    # F -> true | false | "not" F | '(' B ')'
    def rec_F(self):
        if self.symbol == "true":
            return self.rec_terminal(self.symbol)
        elif self.symbol == "false":
            return self.rec_terminal(self.symbol)
        elif self.symbol == "not":
            return self.rec_terminal(self.symbol) and self.rec_F()
        elif self.symbol == '(':
            return self.rec_terminal(self.symbol) and self.rec_B() and self.rec_terminal(')')
        else:
            return False

    # B' -> or B B' | €
    def rec_Bl(self):
        ...

    # T' -> and F T' | €
    def rec_Tl(self):
        ...

    # Funções para interpretar Símbolos Terminais
    def rec_terminal(self, terminal):
        if terminal == self.symbol:
            self.symbol = self.lexer.token()
            return True
        else:
            return False


interpreter = Grammar("true and not(false and not(false))")
if interpreter.rec_Z():
    print("Expressão Válida")
else:
    print("Expressão Inválida")






