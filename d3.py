'''
    Um projeto exige a interação com o usuário através de um menu de opções em modo
texto. Para isso é necessário uma função genérica que recebe como parâmetro uma lista de strings
(correspondendo às opções de um menu) e imprime na tela um menu numerado (a primeira opção
corresponde ao valor 1). Ao final, a opção de sair com zero deve ser impressa também.


Esta função
deve então ficar em repetição, solicitando ao usuário um inteiro e testando se este é válido entre
as escolhas possíveis (incluindo zero). Se a entrada for inválida, deve exibir novamente o menu e
fazer uma nova pergunta. Se for válida deve retornar a escolha feita. Escreva então um programa
para testar essa função de menu, e que implementa as seguintes funcionalidades: “Definir inteiro
A”, “Definir inteiro B”, “Exibir o mínimo múltiplo comum (MMC) entre A e B” e “Exibir o máximo
divisor comum (MDC) entre A e B”.
'''

def menu(lista):
    for i in range(1, len(lista)):
        print(f'{i} - {l_menu[i]}')
    print(f'{0} - {l_menu[0]}')
    opcao = None
    opcao = int(input('Escolha um ítem do menu: '))
    while 0 <= opcao < 5:
        return opcao
l_menu = [
        'Sair', 
        'Definir inteiro A', 
        'Definir inteiro B', 
        'Exibir o mínimo múltiplo comum (MMC) entre A e B', 
        'Exibir o máximo divisor comum (MDC) entre A e B'
        ]
a = None
b = None
opcao = menu(l_menu)
while opcao != 0:
    if opcao == 1:
        a = int(input('Definir inteiro A: '))
        
    if opcao == 2:
        b = int(input('Definir inteiro B: '))
        
    if opcao == 3:
        if a == None and b == None:
            while a == None and b == None:
                print('A não definido')
                a = int(input('Defina inteiro A:'))
                print('B não definido')
                b = int(input('Defina inteiro B:'))
        valor = a*b
        if a < b:
            temp = b
            b = a
            a = temp
            r = a % b
            while r != 0:
                a = b
                b = r
                r = a % b
            valor = valor/b
        print('MMC = ', valor)
            
    if opcao == 4:
        if a == None and b == None:
            while a == None and b == None:
                print('A não definido')
                a = int(input('Defina inteiro A:'))
                print('B não definido')
                b = int(input('Defina inteiro B:'))
        if a < b:
            temp = b
            b = a
            a = temp
            r = a % b
            while r != 0:
                a = b
                b = r
                r = a % b
        elif b < a:
            temp = a
            a = b
            b = temp
            r = b % a
            while r != 0:
                b = a
                a = r
                r = b % a
            b = a
        print('MDC = ', b)
        
    if opcao == 0:
        quit()
    opcao = menu(l_menu)