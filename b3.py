'''
    Faça um procedimento que implementa o Código de César. O código de César é uma
técnica simples de criptografia onde cada letra de um texto é substituída pela que está n posições
à frente do alfabeto (considere apenas as 26 letras maiúsculas, sem acentuação). Esse critério “dá
a volta” após a letra Z. O procedimento deve então receber como parâmetro uma string e um
inteiro, imprimindo a versão codificada. Valide este procedimento fazendo duas chamadas de
teste.
'''

def criptografar(palavra, casas):
    
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    palavra_cripto = ''
    
    for i in palavra:
        a = alfabeto.find(i)
        a += casas
        if a > 25:
            b = a
            a = b - 26
        palavra_cripto += alfabeto[a]
    return palavra_cripto

chamada = 2
while chamada > 0:
    palavra_original = input('Insira uma palavra pra criptografar:')
    palavra_original = palavra_original.upper()
    casas = int(input('Insira um número para as casas: '))

    print(criptografar(palavra_original, casas))
    chamada -= 1
