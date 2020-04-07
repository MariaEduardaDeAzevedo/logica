#coding: utf-8

def encontra_proposicoes(string):
    proposicoes = set()
    for l in string:
        if l.isalpha():
            proposicoes.add(l)
    return proposicoes

def define_valor_bool(string, conjunto):
    for p in conjunto:
        if (p in string) and (f'!{p}' in string):
            return True
    return False

def analisa_clausula(lista):
    valores = list()
    for e in lista:
        proposicoes = encontra_proposicoes(e)
        valores.append(define_valor_bool(e, proposicoes))

    valor = valores[0]
    for i in range(1, len(valores)):
        valor = valor and valores[i]

    if valor:
        return "eh valida"
    
    return "nao eh valida"

numero_de_formulas = int(input())

for i in range(numero_de_formulas):
    formula = str(input())
    clausulas = formula.split("&")
    print(analisa_clausula(clausulas))
