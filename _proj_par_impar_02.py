try:
    entrada = int(input("Digite um número inteiro "))
except:
    print("Você não digitou um número inteiro")
else:
    if entrada % 2 == 0:
        print(f'{entrada} O número que você digitou é par')
    else:
        print(f'{entrada} O número que você digitou é ímpar')
