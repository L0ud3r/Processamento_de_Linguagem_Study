# Exercicio da aula 6 pagina 4


# 1ºPasso: Identificar os elementos do automato
#
# q0 -> Estado Inicial
# F -> Estado Final
# Q -> Todos os estados (Posicoes ao longo da "palavra")
# A -> Alfabeto de carateres/digitos para escrever (O que escrever entre cada estado)
# TT -> Tabela de transições (as possiveis transições entre estados)

q0 = "A"
F = {"C", "E"}   # OU set(["C", "E"])
E = {"A", "B", "C", "D", "E"}
Numbers = {str(x) for x in range(0, 10)}
A = {"+", "-", "."}.union(Numbers)   # Todos os digitos e +, -, .

TT = {}


# 2º Passo: Encher a TT com Errors em todos os elementos
for i in E:
    TT[i] = {}
    for j in A:
        TT[i][j] = "ERROR"


# 3º Passo: Preencher TT com transições do automato
for v in [str(x) for x in range(0, 10)]:
    for q in ["A", "B", "C"]:
        TT[q][v] = "C"
    for q in ["D", "E"]:
        TT[q][v] = "E"


# 4º Passo: Preencher Exceções
TT["A"]["+"] = "B"
TT["A"]["-"] = "B"
TT["C"]["."] = "D"


# 5º Passo: Funcões de leitura de palavras introduzidas (GENÉRICAS)
def read_word(tt, string):
    alfa = q0
    while len(string) > 0 and alfa != "ERROR":
        first_char = string[0]
        if first_char in tt[alfa]:
            alfa = tt[alfa][first_char]
        else:
            alfa = "ERROR"
        string = string[1:]

    return alfa in F and string == ""


def read_string(string):
    alpha = q0
    while len(string) > 0 and alpha != "ERROR":
        current_char = string[0]
        alpha = TT[alpha][current_char] if current_char in A else "ERROR"
        string = string[1:]
    return alpha in F and len(string) == 0


# Introdução de palavras teste
for word in ["42", "3.1415926", "+49.3", "-42", "+3.", "batatas"]:
    r = read_word(TT, word)
    print(f"Read({word}) = {r}")

for teste in ["+3.14", "42", "-54", "-334.41", "5batatas", "cebolas", "1.2.3"]:
    print(f"{teste} => {read_string(teste)}")
