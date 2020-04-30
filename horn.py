#coding:utf-8

'''
Maria Eduarda de Azevedo Silva - 119110210
Lógica para Computação - Prof. Tiago Massoni

Programa que verifica a satisfatibilidade de uma expressão
na fórmula Horn
'''
#Verifica se o lado esquerdo da cláusula é verdadeiro
def eh_verdadeiro(lista):
    for e in lista[:-1]:
        if e == False:
            return False

    return True

#Retorna uma lista apenas com as proposicoes atomicas de uma cláusula
def get_proposicoes_atomicas(clausula):
    proposicoes = clausula.split("&")
    for i in range(len(proposicoes)):
        if "->" in proposicoes[i]:
            proposicoes[i] = proposicoes[i].split("->")
            for j in range(len(proposicoes[i])):
                proposicoes.append(proposicoes[i][j])
            proposicoes.pop(i)
    return proposicoes

#Marca todos os verdadeiros da cláusula
def marca_verdadeiros(clausula):
    proposicoes = get_proposicoes_atomicas(clausula)
    valores = list()
    for e in proposicoes:
        if e.strip() == "T":
            valores.append(True)
        else:
            valores.append(False)

    return valores

#Retorna uma lista com todas as cláusulas da fórmula Horn passada
def get_clausulas(expressao):
    expressao.strip("")
    clausulas = expressao.split(") & (")
    clausulas[0] = clausulas[0][1:]
    clausulas[len(clausulas)-1] = clausulas[-1][:-1]
    return clausulas

#Algoritmo para verificação da satisfatibilidade da fórmula Horn
def horn(formula):
    clausulas = get_clausulas(formula)
    expressao = list()
    marcados = list()
    for clausula in clausulas:
        expressao.append(marca_verdadeiros(clausula))

    finalizado = False
    while not finalizado:
        finalizado = True
        for i in range(len(expressao)):
            proposicoes = get_proposicoes_atomicas(clausulas[i])
            for j in range(len(proposicoes)):
                if proposicoes[j].strip() in marcados:
                    expressao[i][j] = True

            if eh_verdadeiro(expressao[i]) and expressao[i][-1] == False:
                expressao[i][-1] = True
                marcados.append(clausulas[i][-1].strip())
                finalizado = False
    
    if "F" in marcados:
        return False
    return True


# ----------- Programa Principal --------------

numero_formulas = int(input("Entradas: "))
for n in range(numero_formulas):
    status = horn(str(input(f"Fórmula {n + 1}: ")).strip())
    if status:
        print("Satisfazível")
    else:
        print("Insatisfazível")
