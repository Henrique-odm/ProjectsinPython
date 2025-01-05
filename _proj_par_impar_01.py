"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digitar um número
inteiro, informe que não é um númro inteiro.
"""

entrada = input ("Digite um número ")

if entrada.isdigit():
    entrada_int = int(entrada) #informando que a entrada tem que ser inteiro
    par_impar = entrada_int % 2 == 0
    par_impar_texto = "impar" #assumir que a variável será sempre impar

    if par_impar:
        par_impar_texto = "par" #assumir que a variável será sempre par

    print(f"O número {entrada_int} é {par_impar_texto}")

else:
    print("você não digitou um número inteiro")



