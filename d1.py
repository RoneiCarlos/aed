'''
    D1.Um projeto exige fazer operações entre vetores de valores, tal como na Álgebra
Linear. Então você deve projetar funções que recebem duas listas de valores como parâmetro e
que calculam sua adição, subtração e produto interno (também chamado de produto escalar). Os
vetores devem ter o mesmo tamanho (valide antes de fazer o cálculo e imprima uma mensagem de
alerta se for o caso). Escreva então um programa de teste que define três vetores a, b e c (de
tamanho quatro) e que calcula o resultado da seguinte expressão matemática: (a + b) • (c - a),
usando as funções implementadas anteriormente (não é permitido usar funções de biblioteca do
Python).
'''
# função de validação dos 3 vetores
def valida_vetores(v1, v2, v3):
    a = None
    if len(v1) == len(v2) == len(v3):
        a = True
    else:
        a = 'Vetores com tamanhos diferentes!'
    return a

# corre os dois vetores fazendo a soma dos seus ítens e retorna uma lista como resultado
def soma_vetores(v1, v2):
    l_soma = []
    for i in range(0, len(v1)):
        l_soma.append(v1[i]+v2[i])
    return l_soma

# corre os dois vetores fazendo a subtração dos seus ítens e retorna uma lista como resultado
def subtrai_vetores(v1, v2):
    l_subtrai = []
    for i in range(0, len(v1)):
        l_subtrai.append(v1[i]-v2[i])
    return l_subtrai

#corre os dois vetores resultantes da soma e da subtração multiplicando os indices, armazenando em uma outra lista e somando e retornando os índices dessa nova lista
def multiplica_vetores(v1, v2):
    l_multiplica = []
    sm = 0
    for i in range(0, len(v1)):
        l_multiplica.append(v1[i]*v2[i])
    for i in range(0, len(l_multiplica)):
        sm += l_multiplica[i]
    return sm
    
# define as listas e faz a chamada de teste com as listas definidas se elas passarem na validação
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
c = [9, 5, 5, 4]

if valida_vetores(a, b, c) == True:
    
    soma = soma_vetores(a, b)
    subtracao = subtrai_vetores(c, a)
    produto_escalar = multiplica_vetores(soma, subtracao)

    print(produto_escalar)

else:
    print(valida_vetores(a, b, c))
