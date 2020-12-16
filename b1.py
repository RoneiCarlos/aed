'''
    Faça um procedimento que receba como parâmetro uma lista com valores numéricos
reais positivos e encontre tanto a maior como a segunda maior diferença entre dois elementos
consecutivos nesta lista (em valor absoluto). Exiba então quais são os dois pares de elementos e
qual a diferença (em valor absoluto) entre eles. Valide este procedimento fazendo uma chamada
de teste.
'''

# importa o método uniform da biblioteca random, pergunta qual o comoprimento da lista, 
# gera numeros randomicos e os adiciona na lista
from random import uniform

n = int(input('Insira o numero de elementos da lista: '))

print(f'Serão gerados {n} números racionais pseudo-randomicos de 0 até 100')

lista = []
while n > 0: 
        lista.append(round(uniform(0, 100), 2))
        n-=1

def duas_diferencas(lista):
    dif = 0
    
    # calcula as diferenças da lista e as adiciona uma a uma em uma nova lista onde é verificado qual 
    # é a maior diferença entre elas e a exibe junto com os elementos que formam essa diferença 
    # de acordo com o índice desse maior elemento na lista de diferenças
    diferencas = []
    
    for i in range(0, len(lista)-1):
        dif = abs(round((lista[i] - lista[i+1]), 2))
        diferencas.append(dif)
    
    ind_maior = diferencas.index(max(diferencas))

    parte_1 = f'A maior diferença é {diferencas[ind_maior]} da diferença entre {lista[ind_maior]} e {lista[ind_maior+1]}. '

    # corre a lista de diferenças e vai adicionando as diferenças em outra lista e 
    # onde estiver o index da maior diferença da lista adiciona um número negativo
    # acha novamente o index do maior numero agora dessa outra lista sem o primeiro 
    # maior número e armazena os elementos em uma string de acordo com a segunda lista de maior elemento
    diferencas_2 = []

    for i in range(0, len(diferencas)):
        if diferencas[i] == diferencas[ind_maior]:
            diferencas_2.append(-1)
        else:
            diferencas_2.append(diferencas[i])

    ind_segunda_maior = diferencas_2.index(max(diferencas_2))
    
    parte_2 = f'A segunda maior diferença é {diferencas_2[ind_segunda_maior]} da diferença entre {lista[ind_segunda_maior]} e {lista[ind_segunda_maior+1]}.'


    return parte_1+parte_2
print(duas_diferencas(lista))

