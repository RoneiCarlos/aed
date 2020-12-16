'''
Um projeto exige validação de frases escritas em português. Para isso são necessárias
funções que recebem strings como parâmetro e retornam verdadeiro apenas se forem válidas. A
primeira deve testar se apenas a inicial da frase está em letra maiúscula. Outra função deve
validar se a frase termina usando os caracteres '.', '?' ou '!' (ponto final, interrogação ou
exclamação), além de garantir que estes não ocorrem em nenhuma outra parte da frase.
Finalmente, uma terceira função deve garantir que os caracteres ':', ';' e ',' sejam usados
corretamente dentro da frase (caso presentes, não podem estar no final da mesma). Escreva então
um programa que lê uma frase do usuário e indica quais os testes em que a frase passou e quais
em que ela falhou.
'''

def letra_maiuscula(frase):
    l = frase[0]

    ll = l.isupper()
    if ll:
        return True
    else:
        return False

def pontuacao_final(frase):
    
    l_ponto = frase.find('.')
    l_exclamacao = frase.find('!')
    l_interrogacao = frase.find('?')

    if '.' in frase:
        if l_ponto == len(frase)-1:
            return True
        else:
            return False
    elif '!' in frase:
        if l_exclamacao == len(frase)-1:
            return True
        else:
            return False
    elif '?' in frase:
        if l_interrogacao == len(frase)-1:
            return True
        else:
            return False
    else:
        return False

def pontuacao_meio(frase):
    
    l_doispontos = frase.find(':')
    l_pontovirgula = frase.find(';')
    l_virgula = frase.find(',')
    
    if ':' in frase:
        if l_doispontos != len(frase)-1:
            return True
        else:
            return False
    elif ';' in frase:
        if l_pontovirgula != len(frase)-1:
            return True
        else:
            return False
    elif ',' in frase:
        if l_virgula != len(frase)-1:
            return True
        else:
            return False
    else:
        return True


frase = input('insira uma frase: ')

if pontuacao_final(frase):
    print('frase PASSOU no teste de pontuação final!')
else: 
    print('frase FALHOU no teste de pontuação final!')

if pontuacao_meio(frase):
    print('frase PASSOU no teste de pontuação de virgula, dois pontos e ponto e vírgula!')
else:
    print('frase FALHOU no teste de pontuação de virgula, dois pontos e ponto e vírgula!')
        
if letra_maiuscula(frase):
    print('frase PASSOU no teste de primeira letra maiúscula!')
else:
    print('frase FALHOU no teste de primeira letra maiúscula!')

