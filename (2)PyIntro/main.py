# CICLO FOR ------------------------------

# for(int i = 0; i < 10; i++) [para fazer de 2 em 2: for a in range(0, 10, 2): ]
for a in range(0, 10):
    print(a)


# ARRAYS ---------------------------------

meses = ["jan", "fev", "mar", "abr", "mai"]
for a in range(0, len(meses)):
    print(meses[a])


# FUNÇÕES --------------------------------


def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
    # OR
    # return n * fact(n-1) if n > 1 else 1


print(f"Factorial of 4: {fact(4.1)}")


# Linked Lists ---------------------------
# em python syntax de array é igual às listas

# Entre 0 e 10, fazer addList aos fatoriais dos numeros pares
lista = [fact(i) for i in range(0, 10) if i % 2 == 0]
print(lista)


# MANIPULAR STRINGS

def count_chars(string, char):
    return len([s for s in range(0, len(string)) if string[s] == char])


frase = "Eu vi um sapo, um grande sapo!"

# Adicionar extra """" por causa dos " " dentro do print
print(f"""Espaços: {count_chars(frase, " " )}""")
print(f"Letras 'a': {count_chars(frase, 'a')}")
