"""
for i in range(1,11): Usada para criar um loop 

range(início, fim, passo)
início: O valor onde a sequência começa
fim: O valor onde a sequência termina
passo: a quantidade que o valor deve aumentar

início = 1
fim = 11 (a sequência vai até 11, mas não inclui), ou seja, vai até 10!
passo = 1(padrão), aumenta de 1 em 1, então a sequência gerada será: 1,2,3,4,5,6,7,8,9,10

for i: A cada interação, a variável {i} irá assumir um dos valores gerados pela range (1, 11)
"""

try:
    numero = int(input("Digite um número de 1 a 10: "))
    if 1 <= numero <= 10:
        print(f' \ntabuada de {numero}:')
        for i in range(1,11):
            print(f'{numero} x {i} = {numero}')
    else:
        print("Por favor, insira um número entre 1 e 10.")
except ValueError:
    print("Você não digitou um número inteiro")
