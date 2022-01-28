# stack_calculator.py
import ply.lex as lex

from calculadoraPly import Calculadora
class Calculator:

    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def _operator(self, operator):
        if len(self.stack) < 2:
            print("Not enough arguments on stack")
            exit(1)
        second_number = self.stack.pop()
        first_number = self.stack.pop()
        self.push(operator(first_number, second_number))

    def add(self):
        self._operator(lambda a, b: a+b)

    def sub(self):
        self._operator(lambda a, b: a-b)

    def mul(self):
        self._operator(lambda a, b: a*b)

    def div(self):
        if self.top() == 0:
            print("Division by zero")
            exit(1)
        self._operator(lambda a, b: a/b)

    def top(self):
        return self.stack[-1]

# Inicializar e orientar o lexer
lexer = lex.lex()

# iter irá manipular o commandoline (input escreve, nada irá ler)
for line in iter(lambda: input(">> "), ""):
    lexer.input(line)
    stack = Calculator()
    for token in iter(lexer.token, None):
        if token.type == "NUM":
            stack.push(token.value)
        else:
            token.value(stack)
    print(stack.top())